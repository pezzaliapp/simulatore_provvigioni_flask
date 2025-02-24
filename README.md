# 📊 Simulatore di Provvigioni

Questa applicazione Flask consente di calcolare provvigioni, margini e utile netto in base a diverse variabili come sconti applicati, spese aziendali e fatturato stimato.

🚀 Funzionalità Principali
	•	✅ Calcolo del prezzo scontato in base allo sconto inserito.
	•	✅ Calcolo del margine netto considerando un margine lordo standard del 50%.
	•	✅ Calcolo dinamico della provvigione basata sullo sconto applicato:

Sconto Applicato (%)	Provvigione (%)
Fino al 30%	10%
Fino al 40%	7%
Fino al 50%	5%
Oltre il 50%	3%


	•	✅ Inserimento delle spese aziendali:
	•	Costo Auto Aziendale
	•	Spese Carburante
	•	Spese Telepass
	•	Contributo Fisso al Venditore (modificabile)
	•	✅ Inserimento del fatturato mensile stimato.
	•	✅ Calcolo dell’utile netto dopo aver sottratto tutte le spese e le provvigioni.
	•	✅ Download di un file Excel con il riepilogo dei calcoli.

🛠️ Tecnologie Utilizzate
	•	Flask - Framework web in Python
	•	Pandas - Per la creazione e gestione dei dati
	•	Openpyxl - Per generare il file Excel
	•	Gunicorn - Server WSGI per il deploy su Render
	•	Render - Piattaforma per il deploy dell’applicazione

📋 Come Usare l’App
	1.	Apri l’app al seguente link: Simulatore di Provvigioni
	2.	Inserisci i seguenti dati nel form:
	•	Prezzo di Listino
	•	Sconto da applicare
	•	Costi aziendali (Auto, Carburante, Telepass, Contributo Fisso)
	•	Fatturato mensile stimato
	3.	Clicca su “Calcola e Scarica Excel”.
	4.	Verrà generato e scaricato un file Excel con tutti i calcoli dettagliati.

💡 Esempio di Input
	•	Prezzo di Listino: 10.000€
	•	Sconto: 20%
	•	Costo Auto Aziendale: 500€
	•	Spese Carburante: 400€
	•	Spese Telepass: 100€
	•	Contributo Fisso al Venditore: 1.900€
	•	Fatturato Mensile Stimato: 15.000€

📈 Output nel File Excel

Il file generato conterrà le seguenti informazioni:
	•	Prezzo di Listino
	•	Sconto Applicato
	•	Prezzo Scontato
	•	Margine Netto
	•	Provvigione Calcolata
	•	Spese Totali
	•	Margine Aziendale Netto
	•	Fatturato Mensile Stimato
	•	Utile Netto

🔧 Installazione Locale (Opzionale)
	1.	Clona il repository:

git clone https://github.com/pezzaliapp/simulatore_provvigioni_flask.git
cd simulatore_provvigioni_flask


	2.	Crea un ambiente virtuale e attivalo:

python -m venv venv
source venv/bin/activate  # Su Mac/Linux
# oppure
.\venv\Scripts\activate  # Su Windows


	3.	Installa le dipendenze:

pip install -r requirements.txt


	4.	Avvia l’app localmente:

python app.py


	5.	Vai su http://127.0.0.1:5000/ per utilizzare l’app.

📝 Note Finali
	•	Il contributo fisso al venditore è modificabile nel form.
	•	Puoi personalizzare ulteriormente i calcoli aggiornando il file app.py.

👤 Autore: Alessandro Pezzali
🔗 pezzaliAPP.com | alessandropezzali.it
