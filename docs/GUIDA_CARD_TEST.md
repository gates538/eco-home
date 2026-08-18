# Guida alla card Eco Home v1.1.8

La card usa soltanto componenti standard di Home Assistant.

## Requisiti

Prima di installarla verifica che siano presenti:

- l'automazione `Eco home` 1.1.8;
- gli helper indicati in [DIPENDENZE.md](DIPENDENZE.md);
- le entità personali e i dispositivi configurati nella card.

## Installazione

1. Apri la dashboard Home Assistant.
2. Seleziona **Modifica dashboard**.
3. Premi **Aggiungi scheda**.
4. Scegli **Manuale**.
5. Copia tutto il contenuto di `eco-home-v1.1.8-dashboard-card.yaml`.
6. Salva la scheda.

## Sezioni della card

### Controlli

Permette di attivare Eco Home, impostare la modalità silenziosa e vedere se esiste un promemoria asciugatrice.

### Scenario di test

Seleziona il profilo vocale e avvia il test. Consulta [GUIDA_PULSANTE_TEST.md](GUIDA_PULSANTE_TEST.md) per il significato degli scenari.

### Persone e dispositivi

Mostra graficamente:

- Stefano e Laura;
- portone;
- stato e fine prevista dell'asciugatrice;
- Nest Hub.

Se i tuoi entity ID sono diversi, modificali sia nell'automazione sia nella card.

### Diagnostica

Mostra l'ultimo evento ricevuto, l'esito, la persona, il profilo, il messaggio e gli orari principali. I valori sono visualizzati in sola lettura dalla card.

## Primo test consigliato

1. Seleziona `Percorso audio`.
2. Premi il pulsante di test.
3. Verifica che il Nest Hub pronunci il messaggio.
4. Controlla che il volume torni al valore precedente.
5. Controlla `Ultimo esito` nella sezione diagnostica.

## Problemi comuni

- **Entità non disponibile:** correggi l'entity ID nella card.
- **Scenario o diagnostica assenti:** verifica che i 14 helper usino il prefisso `eco_home_*` e non `echo_home_*`.
- **Il pulsante non parla:** controlla lo stato del Nest Hub e `Ultimo esito`.
- **La TV non si silenzia:** verifica che supporti `media_player.volume_mute`.


