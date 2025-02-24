from flask import Flask, render_template, request, send_file
import pandas as pd
import io

app = Flask(__name__)

# Tabella provvigioni basata sullo sconto applicato
provvigioni = [
    (0, 30, 10),
    (31, 40, 7),
    (41, 50, 5),
    (51, 60, 3)
]

# Budget mensile predefinito (modificabile)
budget_mensile = {
    'gennaio': 20319,
    'febbraio': 30485,
    'marzo': 36063,
    'aprile': 29948,
    'maggio': 24699,
    'giugno': 29348,
    'luglio': 33249,
    'agosto': 6086,
    'settembre': 27960,
    'ottobre': 34167,
    'novembre': 43821,
    'dicembre': 33855
}

# Contributo fisso mensile per il venditore
contributo_fisso = 1900

@app.route('/')
def index():
    return render_template('index.html', mesi=budget_mensile.keys())

@app.route('/calcola', methods=['POST'])
def calcola():
    prezzo_listino = float(request.form['prezzo_listino'])
    sconto_applicato = float(request.form['sconto_applicato'])
    costi_totali = float(request.form['costi_totali'])
    mese_selezionato = request.form['mese']

    # Calcolo Prezzo Scontato
    prezzo_scontato = prezzo_listino * (1 - sconto_applicato / 100)

    # Calcolo Provvigione
    provvigione = 0
    for sc_min, sc_max, perc in provvigioni:
        if sc_min <= sconto_applicato <= sc_max:
            provvigione = prezzo_scontato * (perc / 100)
            break

    # Calcolo Utile Netto
    utile_netto = prezzo_scontato - provvigione - costi_totali

    # Calcolo Scostamento dal Budget basato sul Prezzo Scontato
    budget_mese = budget_mensile[mese_selezionato]
    scostamento_budget = prezzo_scontato - budget_mese

    # Calcolo Compenso Effettivo Venditore (Contributo fisso + Provvigione)
    compenso_effettivo = contributo_fisso + provvigione

    # Creazione DataFrame per l'output
    dati = {
        'Descrizione': [
            'Prezzo Listino', 'Prezzo Scontato', 'Sconto Applicato (%)',
            'Provvigione', 'Costi Totali', 'Utile Netto',
            'Budget Mensile', 'Scostamento Budget', 'Compenso Effettivo Agente'
        ],
        'Valore': [
            prezzo_listino, prezzo_scontato, sconto_applicato,
            provvigione, costi_totali, utile_netto,
            budget_mese, scostamento_budget, compenso_effettivo
        ]
    }
    df = pd.DataFrame(dati)

    # Salva il file Excel in memoria
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)
    output.seek(0)

    return send_file(output, as_attachment=True, download_name='simulazione_provvigioni.xlsx', mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

if __name__ == '__main__':
    app.run(debug=True)