# Guida di Aggiornamento a Eco Home 1.1.7

Questa guida descrive la procedura per aggiornare Eco Home alla versione **1.1.7** da una versione precedente.

La versione 1.1.7 introduce il monitoraggio della temperatura media interna all'arrivo e l'opzione di accendere i condizionatori tramite notifica push interattiva sul cellulare se si superano i 26°C.

---

## 1. Crea la cartella degli snapshot
Per consentire a Home Assistant di salvare le immagini scattate dalla telecamera, devi creare la cartella per gli snapshot:
1. Accedi ai file del tuo Home Assistant (tramite Samba, SSH o l'add-on Studio Code Server).
2. All'interno della cartella `/config/www/`, crea una nuova cartella chiamata `snapshots` (il percorso completo sarà `/config/www/snapshots/`).
   * *Nota*: Se la cartella `www` non esiste, creala e riavvia Home Assistant prima di procedere.

---

## 2. Aggiorna o crea il nuovo helper

### Se usi i Package YAML (Consigliato)
1. Rimuovi il vecchio file package `eco-home-v1.1.6-helpers.yaml` (o precedenti) da `/config/packages/`.
2. Copia il nuovo file `eco-home-v1.1.7-helpers.yaml` nella stessa cartella.
3. Ricarica i package o riavvia Home Assistant.

### Se hai creato gli helper dalla UI
Se preferisci gestire gli helper manualmente dalla UI di Home Assistant, vai in **Impostazioni → Dispositivi e servizi → Aiutanti** e crea il nuovo helper mancante:
* **Tipo**: Interruttore (input_boolean)
* **Nome**: Eco Home notifiche foto
* **Entity ID generato**: `input_boolean.eco_home_notifiche_foto`
* **Icona**: `mdi:camera`

---

## 3. Aggiorna l'automazione
Apri il tuo file `/config/automations.yaml` ed individua il blocco dell'automazione Eco Home (puoi cercarlo tramite l'id `'1783777716602'`).
1. Sostituisci **esclusivamente** il blocco dell'automazione esistente con il contenuto di [eco-home-v1.1.7.yaml](eco-home-v1.1.7.yaml).
2. Modifica le variabili in fondo al file (nella sezione `variables:`) per impostare la tua telecamera (default: `camera.sala_2`) e i tuoi canali di notifica push (es. `notify.mobile_app_tuo_telefono`).
3. Salva il file e vai su **Strumenti per sviluppatori → YAML** e clicca su **Ricarica le automazioni**.

---

## 4. Aggiorna la card Lovelace
Apri la plancia di Home Assistant, clicca sui tre puntini in alto a destra → **Modifica plancia**.
1. Trova la card di Eco Home, clicca su **Modifica** e poi su **Editor di codice**.
2. Sostituisci il codice YAML esistente con il contenuto di [eco-home-v1.1.7-dashboard-card.yaml](eco-home-v1.1.7-dashboard-card.yaml).
3. Clicca su **Salva** e poi su **Fatto**.

---

## 5. Verifica del funzionamento
1. Vai sulla dashboard di Eco Home e attiva il nuovo interruttore **Notifiche con foto**.
2. Esegui un test selezionando lo scenario `Percorso audio` o `Rientro Stefano` dalla card e cliccando su **Avvia il test**.
3. Verifica in `/config/www/snapshots/` se l'immagine temporanea viene correttamente creata.
4. Controlla che i telefoni ricevano la notifica push con lo snapshot allegato.
