# Changelog

Tutte le modifiche rilevanti di Eco Home sono documentate in questo file.

## [1.1.2] - 2026-07-13

### Corretto

- Il messaggio può partire sia con `persona home → portone` sia con `portone → persona home`.
- Il trigger `person_arrived` viene ora accettato quando il portone è stato aperto recentemente.
- La chiusura del portone non annulla più la conferma mentre si attende l'aggiornamento della posizione.
- L'identità viene determinata tramite `person.stefano` e `person.laura`, evitando i nomi completi configurati come `friendly_name`.

### Migliorato

- Aggiunti nomignoli casuali maschili per Stefano.
- Aggiunti nomignoli casuali femminili per Laura.
- Aggiunti nomignoli casuali di coppia quando entrambi rientrano insieme.
- Aggiornati README, card Lovelace e guide per descrivere la logica bidirezionale.

### Compatibilità

- Nessun nuovo helper richiesto.
- Nessuna nuova entità richiesta.
- Le configurazioni della versione 1.1.1 restano compatibili.

## [1.1.1] - 2026-07-13

### Aggiunto

- Prima versione pubblica con conferma tramite presenza e portone.
- Messaggi locali casuali, gestione Nest Hub, luce, TV e asciugatrice.
- Pulsante di test vocale, card Lovelace e diagnostica nel Logbook.


