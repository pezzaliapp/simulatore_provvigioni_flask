from flask import Flask, render_template, request, send_file
import pandas as pd
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcola', methods=['POST'])
def calcola():
    prezzo_listino = float(request.form['prezzo_listino'])
    sconto = float(request.form['sconto'])
    margine_lordo = 0.5  # Margine lordo standard

    prezzo_scontato = prezzo_listino * (1 - sconto / 100)
    margine_netto = prezzo_listino * margine_lordo - (prezzo_listino - prezzo_scontato)

    # Calcolo provvigione basata sullo sconto
    if sconto <= 30:
        provvigione_percentuale = 0.10
    elif sconto <= 40:
        provvigione_percentuale = 0.07
    elif sconto <= 50:
        provvigione_percentuale = 0.05
    else:
        provvigione_percentuale = 0.03

    provvigione = prezzo_scontato * provvigione_percentuale
    margine_azienda = margine_netto - provvigione

    # Creazione DataFrame
    df = pd.DataFrame({
        'Prezzo Listino': [prezzo_listino],
        'Sconto (%)': [sconto],
        'Prezzo Scontato': [prezzo_scontato],
        'Margine Netto': [margine_netto],
        'Provvigione (%)': [provvigione_percentuale * 100],
        'Provvigione (€)': [provvigione],
        'Margine Azienda Netto': [margine_azienda]
    })

    # Salvataggio del file Excel in memoria
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)
    output.seek(0)

    return send_file(output, as_attachment=True, download_name="calcolo_provvigioni.xlsx", mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

if __name__ == '__main__':
    app.run(debug=True)