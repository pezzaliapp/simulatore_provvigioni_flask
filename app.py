from flask import Flask, render_template, request, send_file
import pandas as pd
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcola', methods=['POST'])
def calcola():
    # Dati inseriti dall'utente
    prezzo_listino = float(request.form['prezzo_listino'])
    sconto = float(request.form['sconto'])
    costo_auto = float(request.form['costo_auto'])
    costo_carburante = float(request.form['costo_carburante'])
    costo_telepass = float(request.form['costo_telepass'])
    contributo_fisso = float(request.form['contributo_fisso'])
    fatturato_stimato = float(request.form['fatturato_stimato'])

    margine_lordo = 0.5  # Margine lordo standard

    # Calcoli base
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

    # Calcolo delle spese totali
    spese_totali = costo_auto + costo_carburante + costo_telepass + contributo_fisso

    # Margine aziendale dopo spese e provvigioni
    margine_azienda = margine_netto - provvigione - spese_totali

    # Calcolo copertura costi rispetto al fatturato stimato
    utile_netto = fatturato_stimato - (spese_totali + provvigione)

    # Creazione DataFrame per Excel
    df = pd.DataFrame({
        'Prezzo Listino': [prezzo_listino],
        'Sconto (%)': [sconto],
        'Prezzo Scontato': [prezzo_scontato],
        'Margine Netto': [margine_netto],
        'Provvigione (%)': [provvigione_percentuale * 100],
        'Provvigione (€)': [provvigione],
        'Spese Auto (€)': [costo_auto],
        'Spese Carburante (€)': [costo_carburante],
        'Spese Telepass (€)': [costo_telepass],
        'Contributo Fisso (€)': [contributo_fisso],
        'Spese Totali (€)': [spese_totali],
        'Margine Azienda Netto': [margine_azienda],
        'Fatturato Stimato (€)': [fatturato_stimato],
        'Utile Netto (€)': [utile_netto]
    })

    # Salvataggio del file Excel in memoria
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)
    output.seek(0)

    return send_file(output, as_attachment=True, download_name="calcolo_provvigioni.xlsx", mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

if __name__ == '__main__':
    app.run(debug=True)