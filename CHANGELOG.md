# Changelog

Tutte le modifiche rilevanti di Eco Home sono documentate in questo file.

## [1.4.3] - 2026-07-30

### Nuove Caratteristiche & Miglioramenti Avanzati
- **Voce Femminile Italiana Nativa**: Forzata la lingua ed il dominio italiano (`language: "it"`, `options: { tld: "it" }`) in tutte le chiamate TTS (`EcoHome.yaml`, `cucina.yaml`, `frigo_meteo.yaml`), garantendo una voce femminile naturale, fluida ed in italiano nativo.
- **Tracciamento Esteso Persone (Rita & Mauro)**: Registrati e tracciati Rita (`person.rita`) e Mauro (`person.mauro`) con helper dedicati (`input_boolean.eco_home_saluti_rita` e `input_boolean.eco_home_saluti_mauro`) e logica di rientro integrata.
- **Allerta Porta Freezer Sarcastica**: Creata l'automazione allerta per la porta del congelatore (`binary_sensor.cucina_frigorifero_freezer_door`) con battute esilaranti e scherzose dopo 60 secondi di apertura.
- **Fix Definitivo Annunci Cucina**:
  - Eliminati i trigger sui singoli fuochi per evitare annunci ad ogni cambio di potenza.
  - Ascolto esclusivo dello stato generale del piano ad induzione (`sensor.cucina_piano_cottura_stato_di_funzionamento` da `ready` a `run`) per 1 solo annuncio ad inizio sessione.
  - Impostato un blocco ferreo di 2 ore (`7200s`) per gli annunci della cucina ed eliminati i trigger dal pulsante di test.
- **Fix Definitivo Saluti al Rientro al Portone**:
  - Risolto un bug nel template Jinja (`states[person_id].from_state`) che bloccava la conferma di arrivo.
  - Elevato il cooldown dei saluti di rientro a 15 minuti (`900s`) per prevenire falsi annunci aprendo la porta da dentro.
- **Riorganizzazione Frigo & Meteo**: Ripristinata ed aggiornata l'automazione `frigo_meteo.yaml` per allerta porta frigorifero aperta (>60s) con frasi sarcastiche e notifiche per pioggia/vento in terrazza.

## [1.4.2] - 2026-07-26

### Nuove Caratteristiche & Miglioramenti Avanzati
- **Regola d'Oro Casa Vuota**: Blindatura completa che impedisce qualsiasi annuncio vocale TTS sul Nest Hub se nessuno è fisicamente a casa (`person.*` home == 0).
- **Tracciamento Persone Esteso**: Aggiunto tracciamento di presenza ed accoglienza vocale al rientro per **Simone Mancini** (`person.simone`) e **Monica** (`person.monica`).
- **Interruttore Saluti Mauro**: Aggiunto `input_boolean.eco_home_saluti_mauro` per abilitare/disabilitare dall'interfaccia gli annunci vocali per Mauro ed evitare falsi positivi dal piano superiore.
- **Notifica Clima con Conferma Esplicita**: Notifiche interattive su smartphone per caldo (>26°C) e freddo (<19°C) con pulsanti di conferma esplicita (*Sì, Accendi Clima* / *No, Finestre Aperte*) prima di eseguire qualsiasi azione, evitando sprechi energetici.
- **Automazione Dobby Robot Vacuum (Dreame L40 Pro)**: Pausa e ritorno automatico alla base di Dobby non appena qualcuno rientra a casa, più controlli di stato e batteria integrati nella scheda Lovelace.
- **Report Settimanale Batterie Scariche**: Controllo automatico ogni lunedì alle 10:00 con invio report WhatsApp e avviso vocale se un sensore ha la batteria < 15%.
- **Pet Alert Crocchette (Piccola & Luna)**: Annunci vocali personalizzati ogni volta che il dispenser Petkit eroga il pasto.
- **Promemoria Carburante Auto (Discovery / Drivvo)**: Avviso vocale domenicale alle 20:30 per verificare l'autonomia prima dell'inizio della settimana.
- **Sarcasmo Culinario per Laura**: Frasi esilaranti, ironiche e variegate ad ogni accensione dei fornelli sia per Chef Laura che per Chef Stefano.


## [1.2.0] - 2026-07-18

### Modularizzazione e Nuove Feature
- Suddivisione dell'automazione in più file modulari: `eco-home-v1.2.0-core.yaml`, `eco-home-v1.2.0-security.yaml`, `eco-home-v1.2.0-climate.yaml`.
- Gestione Invernale: Notifica al rientro se la temperatura interna è sotto i 18°C per suggerire l'accensione del riscaldamento.
- Integrazione Meteo e Allerte: Annuncio automatico in caso di pioggia (`weather.home`) o allerte meteo in corso (`sensor.allerta_meteo`).
- Modalità Notte Dinamica: Tra le 23:00 e le 06:00 l'illuminazione si accende al 15% (luce calda a 2200K) e il TTS viene sospeso automaticamente.
- Modalità Ospiti: Aggiunto `input_boolean.eco_home_ospiti`. Se abilitato, disattiva il TTS all'arrivo.
- Guardiano Uscite: Quando la casa si svuota (`zone.home` a 0) notifica eventuali luci dimenticate accese, finestre aperte o elettrodomestici in funzione, offrendo azioni rapide.
- Sistema Anti-Intrusione: Se il portone viene aperto a casa vuota e allarme inserito, scatta una foto, spara il volume al 100% e annuncia l'intrusione inviando notifica push.
- Risparmio Energetico Clima: L'automazione ferma automaticamente i condizionatori se una finestra resta aperta per più di 3 minuti.
- Aggiornate le Dashboard Lovelace con controlli per la Modalità Ospiti e lo stato dell'Allarme.

## [1.1.8] - 2026-07-18

### Consolidamento e Sicurezza (Codex Review)
- Estrazione dell'azione di accensione condizionatori in un'automazione separata (`eco-home-v1.1.8-actions.yaml`) per evitare ritardi con la coda TTS.
- Aggiunto `context.id` univoco per le notifiche interattive, prevenendo attivazioni accidentali da vecchie notifiche.
- Salvataggio degli snapshot telecamera in `/media/eco_home/` anziché `/config/www/` per ragioni di privacy.
- Risolto bug di duplicazione notifiche al rientro di coppia se entrambi usano lo stesso servizio.
- Completa applicazione delle variabili configurabili alle azioni dell'automazione.
- Migliorata diagnostica TTS rimuovendo l'occultamento degli errori.
- Corretti colori nella dashboard Tutta Casa per segnalare esiti OK non solo in presenza della parola 'successo'.
- Aggiunta licenza MIT e validatore YAML in GitHub Actions.

## [1.1.7] - 2026-07-17

### Aggiunto
- Monitoraggio della temperatura media interna all'arrivo basato su una lista configurabile di sensori (`indoor_temp_sensors`).
- Annuncio vocale della temperatura corrente tramite Nest Hub durante il benvenuto.
- Notifica push interattiva (actionable notification) al rientro se la temperatura interna è maggiore di 26°C, chiedendo se si desidera accendere i condizionatori.
- Gestione automatica del clic sulla notifica per accendere i condizionatori (`ac_climate_entities`) in modalità raffrescamento (`cool`).

## [1.1.7] - 2026-07-17

### Corretto
- Rimosso il ritardo fisso di 3 secondi (`arrival_group_window_seconds: 0`) prima dell'annuncio vocale di benvenuto, che ora si attiva immediatamente dopo la conferma di rientro.
- Aggiornati i riferimenti interni e i numeri di riga in tutta la documentazione per allinearli alla versione corrente.

## [1.1.6] - 2026-07-15

### Aggiunto

- Funzionalità di scatto foto (snapshot) tramite telecamera (`camera.sala_2` / "Cam Sala 2") e invio di notifica push ricca con immagine sul cellulare al rientro.
- La notifica viene inviata **solo se la casa era vuota** prima del rientro rilevato (ossia quando Stefano, Laura o persone future non erano in casa).
- Nuovo helper `input_boolean.eco_home_notifiche_foto` per abilitare/disabilitare le notifiche con foto direttamente dalla dashboard.
- Configurazione flessibile per mappare i servizi di notifica individuali (es. `notify.mobile_app_stefano` o `notify.notify` per broadcast).
- Nuova sezione dedicata nella plancia Lovelace per controllare lo stato delle notifiche con foto e visualizzare l'anteprima della telecamera.
- Nuova plancia Lovelace completa [eco-home-v1.1.8-dashboard-tuttacasa.yaml](eco-home-v1.1.8-dashboard-tuttacasa.yaml) per controllare l'intero ecosistema di Home Assistant (clima, luci, presenze, telecamere, elettrodomestici e diagnostica).
- Documentazione completa aggiornata (`README.md`, `DIPENDENZE.md`, `REQUISITI_HARDWARE.md`, `GUIDA_PERSONALIZZAZIONE.md`, `GUIDA_AGGIORNAMENTO.md`).

## [1.1.5] - 2026-07-13

### Corretto

- Sostituito ovunque il prefisso incoerente `echo_home_*` con `eco_home_*`.
- Allineati automazione, card, package helper, variabili interne, messaggi,
  diagnostica e documentazione al nome **Eco Home**.
- Gli helper creati dalla UI ora ricevono naturalmente gli stessi Entity ID
  utilizzati dall'automazione.

### Migrazione

- Aggiunta la procedura completa per rinominare i 14 helper esistenti senza
  duplicarli.
- Aggiunta una guida dedicata alla creazione degli helper dalla UI.
- La logica funzionale della 1.1.3 resta invariata.
- Le versioni archiviate conservano il prefisso storico perché rappresentano
  fedelmente le release precedenti.

## [1.1.3] - 2026-07-13

### Aggiunto

- Selettore con sei scenari di test: percorso audio, Stefano, Laura, coppia, notte e asciugatrice.
- Diagnostica persistente con ultimo evento, esito, profilo, messaggio, persona, apertura del portone e arrivo.
- Card con riepilogo grafico di persone, portone, asciugatrice e Nest Hub.
- Package completo degli helper e package incrementale per chi aggiorna dalla 1.1.2.
- Guida specifica per diagnostica e aggiornamento.

### Migliorato

- Il volume precedente del Nest Hub viene salvato e ripristinato dopo il TTS.
- Il test vocale usa le stesse liste di frasi e nomignoli dell'annuncio reale.
- Gli stati `unknown` e `unavailable` vengono esclusi dai trigger di arrivo e portone.
- Quando il Nest Hub non è disponibile, l'automazione evita il TTS e registra chiaramente l'esito.
- Il promemoria asciugatrice viene consumato soltanto dopo un annuncio eseguito.

### Compatibilità

- Gli helper della 1.1.2 restano validi.
- Sono necessari nuovi helper diagnostici e `input_select.echo_home_scenario_test`.
- Gli entity ID e la logica presenza-portone della 1.1.2 restano compatibili.

## [1.1.2] - 2026-07-13

### Corretto

- Il messaggio può partire sia con `persona home → portone` sia con `portone → persona home`.
- Il trigger `person_arrived` viene accettato quando il portone è stato aperto recentemente.
- La chiusura del portone non annulla la conferma mentre si attende l'aggiornamento della posizione.
- L'identità viene determinata tramite `person.stefano` e `person.laura`.

### Migliorato

- Aggiunti nomignoli casuali maschili, femminili e di coppia.
- Archiviate le versioni precedenti in cartelle separate.

## [1.1.1] - 2026-07-13

### Aggiunto

- Prima versione pubblica con conferma tramite presenza e portone.
- Messaggi locali casuali, gestione Nest Hub, luce, TV e asciugatrice.
- Pulsante di test vocale, card Lovelace e diagnostica nel Logbook.

