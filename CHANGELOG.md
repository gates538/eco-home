# Changelog

Tutte le modifiche rilevanti di Eco Home sono documentate in questo file.

## [2.0.0] - 2026-11-08

### Allineamento Completo v2.0, AI Multimodale (Gemini Vision & TTS), Self-Healing & Sanitizzazione Totale
- **Sincronizzazione Integrale (102 Automazioni & 105 Script)**:
  - Allineati tutti i 7 moduli in `/automations` e i 6 moduli in `/scripts` con l'architettura di produzione attuale.
  - Archiviata la precedente release modulare in `archive/v1.5.0`.
- **Motore AI Multimodale & Annunci Generativi**:
  - Aggiunti gli script di analisi visiva AI (`analizza_telecamera_con_vision_ai`, `ispeziona_terrazzi_ai`, `ispeziona_varco_ai`, `analizza_video_movimento_ai`, `cerca_auto_autonoma_ptz`, `verifica_fiamma_camino_ai`, `riconosci_auto_ospiti_ai`).
  - Aggiunti gli annunci vocali generativi AI su Google Nest Hub (`annuncio_rientro_ai`, `annuncio_cucina_ai`, `annuncio_frigo_ai`, `annuncio_buongiorno_ai`, `buongiorno_weekend_ai`, `annuncio_rifiuti_ore_21_ai`, `annuncio_ospite_ai`, `pillola_sarcastica_nesthub`) con gestione automatica dei volumi (`audio_annuncio_prepara` / `audio_annuncio_ripristina`).
  - Aggiunti i report vocali on-demand (`stato_finestre_porte_aperte`, `stato_acqua_calda_vocale`, `stato_gatte_vocale`, `stato_elettrodomestici_energia_vocale`, `stato_camino_vocale`, `stato_pioggia_pluviometro`, `stato_vento_anemometro`, `spesa_leggi_lista_vocale`).
- **Clima, Termocamino & Ospiti**:
  - Notifica interattiva pre-pranzo per l'accensione del Termocamino a pellet con gestione posticipo (+10/+15/+20 min o avvio automatico differito).
  - Modalità Ospiti Cameretta con isolamento automatico di luci/tapparella/clima, disattivazione telecamera interna per privacy e sincronizzazione Boost Acqua Calda Sanitaria su pompa di calore.
- **Infrastruttura, Self-Healing & Sicurezza**:
  - Watchdog automatico Zigbee2MQTT + coordinatore SLZB-06, auto-healing Wi-Fi Mesh per telecamere, protezione anti-spegnimento prese critiche (NAS/UPS), aggiornamento settimanale container Docker e nightly update HACS.
  - Rilevamento tentativi di accesso HTTP falliti con pulsante di Ban IP immediato da notifica push.
- **Privacy & Anonimizzazione Completa**:
  - Rimossi e sostituiti con placeholder generici tutti i nomi e cognomi reali, soprannomi, indirizzi, comuni, SSID Wi-Fi, domini, sottoreti IP e modelli specifici di veicoli in tutto il repository (inclusi `docs/` e `archive/`).

## [1.5.0] - 2026-08-18

### Riorganizzazione Modulare, Affidabilità & Personalizzazione Avanzata
- **Riorganizzazione Struttura Repository**: Progetto ripulito con alberatura ordinata divisa in `/automations`, `/docs`, `/scripts` e `/archive`.
- **Risoluzione Race Condition Rientri di Coppia**: Configurato `mode: queued` (con `max: 10`) nel modulo principale (`eco-home-v1.5.0-core.yaml`), risolvendo il mutismo del Nest Hub causato dall'accavallamento di trigger simultanei.
- **Armonizzazione TTS Voce Femminile Vivace**: Uniformate tutte le 16 chiamate `tts.speak` su `tts.google_translate_it_lt` con `language: "it"` e `options: { tld: "it" }` per un timbro femminile chiaro, veloce e naturale in ogni modulo.
- **Personalizzazione Sartoriale Routine & Casa**: 
  - Integrazione routine lavorative (pausa pranzo Utente 1, rientro Utente 2 alle 18:40, weekend).
  - Riferimenti affettuosi e divertenti alle gatte **Gatto 1 e Gatto 2** (abitudini sul lettone, Gatto 2 nel lavandino del bagnetto).
  - Gestione specifica impianto di riscaldamento (termocamino a pellet / termosifoni) e climatizzazione estiva (18000 BTU sala + dual split camere).
  - Adattamento vocabolario locale a misura di "paese".
- **Espansione Sarcasmo & Allerte Vocali**: Arricchito il repertorio di battute casuali per allerta vento forte in terrazza, pioggia, cucina/fornelli, frigo/freezer aperti, cottura dimenticata, asciugatrice e dispenser pappa.
- **Sicurezza e Privacy Dati**: Pulizia e sanitizzazione del repository con esclusione credenziali e script locali tramite `.gitignore`.

## [1.4.3] - 2026-07-30

### Nuove Caratteristiche & Miglioramenti Avanzati
- **Voce Femminile Italiana Nativa**: Forzata la lingua ed il dominio italiano (`language: "it"`, `options: { tld: "it" }`) in tutte le chiamate TTS, garantendo una voce femminile naturale, fluida ed in italiano nativo.
- **Tracciamento Esteso Persone (Familiare 3 & Familiare 4)**: Registrati e tracciati Familiare 3 (`person.familiare_3`) e Familiare 4 (`person.familiare_4`) con helper dedicati (`input_boolean.eco_home_saluti_rita` e `input_boolean.eco_home_saluti_mauro`) e logica di rientro integrata.
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
- **Tracciamento Persone Esteso**: Aggiunto tracciamento di presenza ed accoglienza vocale al rientro per **Familiare 2** (`person.familiare_2`) e **Familiare 1** (`person.familiare_1`).
- **Interruttore Saluti Familiare 4**: Aggiunto `input_boolean.eco_home_saluti_mauro` per abilitare/disabilitare dall'interfaccia gli annunci vocali per Familiare 4 ed evitare falsi positivi dal piano superiore.
- **Notifica Clima con Conferma Esplicita**: Notifiche interattive su smartphone per caldo (>26°C) e freddo (<19°C) con pulsanti di conferma esplicita (*Sì, Accendi Clima* / *No, Finestre Aperte*) prima di eseguire qualsiasi azione, evitando sprechi energetici.
- **Automazione Dobby Robot Vacuum (Dreame L40 Pro)**: Pausa e ritorno automatico alla base di Dobby non appena qualcuno rientra a casa, più controlli di stato e batteria integrati nella scheda Lovelace.
- **Report Settimanale Batterie Scariche**: Controllo automatico ogni lunedì alle 10:00 con invio report WhatsApp e avviso vocale se un sensore ha la batteria < 15%.
- **Pet Alert Crocchette (Gatto 1 & Gatto 2)**: Annunci vocali personalizzati ogni volta che il dispenser Petkit eroga il pasto.
- **Promemoria Carburante Auto (Auto Utente 1 / Drivvo)**: Avviso vocale domenicale alle 20:30 per verificare l'autonomia prima dell'inizio della settimana.
- **Sarcasmo Culinario per Utente 2**: Frasi esilaranti, ironiche e variegate ad ogni accensione dei fornelli sia per Chef Utente 2 che per Chef Utente 1.


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
- La notifica viene inviata **solo se la casa era vuota** prima del rientro rilevato (ossia quando Utente 1, Utente 2 o persone future non erano in casa).
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

- Selettore con sei scenari di test: percorso audio, Utente 1, Utente 2, coppia, notte e asciugatrice.
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
- L'identità viene determinata tramite `person.utente_1` e `person.utente_2`.

### Migliorato

- Aggiunti nomignoli casuali maschili, femminili e di coppia.
- Archiviate le versioni precedenti in cartelle separate.

## [1.1.1] - 2026-07-13

### Aggiunto

- Prima versione pubblica con conferma tramite presenza e portone.
- Messaggi locali casuali, gestione Nest Hub, luce, TV e asciugatrice.
- Pulsante di test vocale, card Lovelace e diagnostica nel Logbook.

