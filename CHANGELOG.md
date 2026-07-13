# Changelog

Tutte le modifiche rilevanti di Eco Home sono documentate in questo file.

## [1.1.4] - 2026-07-13

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

