from flask import Flask, render_template, request, send_file
import pandas as pd
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcola', methods=['POST'])
def calcola():
    try:
        # Recupero dei dati dal form
        prezzo_listino = float(request.form.get('prezzo_listino', 0))
        sconto_applicato = float(request.form.get('sconto_applicato', 0))
        costo_auto = float(request.form.get('costo_auto', 0))
        costo_carburante = float(request.form.get('costo_carburante', 0))
        costo_telepass = float(request.form.get('costo_telepass', 0))
        contributo_fisso = float(request.form.get('contributo_fisso', 0))
        fatturato_mensile = float(request.form.get('fatturato_mensile', 0))

        # Calcolo prezzo scontato
        prezzo_scontato = prezzo_listino * (1 - sconto_applicato / 100)

        # Calcolo costi totali
        costi_totali = costo_auto + costo_carburante + costo_telepass + contributo_fisso

        # Calcolo fatturato minimo richiesto
        fatturato_minimo = costi_totali / 0.3  # ipotizzando un margine del 30%

        # Calcolo sconto massimo concedibile
        sconto_massimo = 100 * (1 - (costi_totali / prezzo_listino))

        # Creazione del DataFrame per l'output Excel
        dati = {
            'Descrizione': ['Prezzo Listino', 'Prezzo Scontato', 'Sconto Applicato (%)', 'Costi Totali', 'Fatturato Minimo', 'Sconto Massimo Concedibile (%)'],
            'Valore': [prezzo_listino, prezzo_scontato, sconto_applicato, costi_totali, fatturato_minimo, sconto_massimo]
        }
        df = pd.DataFrame(dati)

        # Creazione del file Excel in memoria
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Calcoli')
        output.seek(0)

        # Invio del file Excel all'utente
        return send_file(output, as_attachment=True, download_name='calcolo_provvigioni.xlsx', mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    except Exception as e:
        return f"Errore durante il calcolo: {e}"

if __name__ == '__main__':
    app.run(debug=True)