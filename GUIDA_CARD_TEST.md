# Guida alla card di test - Eco Home v1.1.2

Questa guida spiega come aggiungere alla plancia di Home Assistant la card di controllo e come utilizzarla per verificare Eco Home v1.1.2.

## Funzioni della card

La card permette di:

- attivare o disattivare Eco Home;
- abilitare o disabilitare la modalita' silenziosa;
- controllare se esiste un promemoria dell'asciugatrice in attesa;
- vedere la data e l'ora dell'ultimo annuncio;
- avviare manualmente un test vocale sul Nest Hub.

## File necessario

Usa il file:

```text
eco-home-v1.1.2-dashboard-card.yaml
```

## Prerequisiti

Prima di aggiungere la card, assicurati che Eco Home v1.1.2 e i suoi helper siano gia' installati.

La card utilizza queste entita':

```text
input_boolean.echo_home_attivo
input_boolean.echo_home_silenzioso
input_boolean.echo_home_asciugatrice_da_annunciare
input_datetime.echo_home_ultimo_annuncio
input_button.echo_home_test_vocale
```

Puoi controllarne l'esistenza da:

**Impostazioni → Dispositivi e servizi → Entita'**

Se una di queste entita' non esiste, installa prima gli helper contenuti in:

```text
packages/eco-home-helpers-v1.1.yaml
```

Gli helper della versione 1.1 sono compatibili con Eco Home v1.1.2.

## Installazione della card

1. Apri Home Assistant.
2. Entra nella plancia in cui vuoi mostrare Eco Home.
3. Premi i tre puntini in alto a destra.
4. Seleziona **Modifica plancia**.
5. Premi **Aggiungi scheda**.
6. Cerca e seleziona la scheda **Manuale**.
7. Apri il file `eco-home-v1.1.2-dashboard-card.yaml`.
8. Copia tutto il suo contenuto.
9. Incollalo nell'editor YAML della scheda manuale.
10. Premi **Salva**.
11. Premi **Fine** per uscire dalla modifica della plancia.

La card non richiede componenti personalizzati o installazioni tramite HACS.

## Come utilizzare la card

### Eco Home attivo

Il controllo **Eco Home attivo** abilita o disabilita gli annunci automatici.

- Attivo: Eco Home puo' eseguire il messaggio di benvenuto.
- Disattivato: gli annunci automatici vengono ignorati.

Per il normale utilizzo deve essere attivo.

### Modalita' silenziosa

Il controllo **Modalita silenziosa** blocca i messaggi automatici senza disattivare completamente il progetto.

- Attiva: nessun messaggio automatico di benvenuto.
- Disattivata: gli annunci possono essere riprodotti normalmente.

E' utile quando non vuoi essere disturbato, per esempio durante una chiamata o nelle ore di riposo.

### Promemoria asciugatrice in attesa

Questa voce indica se Eco Home ha memorizzato un ciclo dell'asciugatrice terminato mentre non era presente nessuno.

- Attivo: il promemoria verra' inserito nel prossimo messaggio valido di rientro.
- Disattivato: non ci sono promemoria da annunciare.

### Ultimo annuncio

La voce **Ultimo annuncio** mostra quando e' stato eseguito l'ultimo messaggio automatico valido.

Serve anche per verificare il periodo di pausa tra due annunci consecutivi.

### Avvia test vocale

Premi una sola volta il pulsante **Avvia test vocale**.

Il test verifica:

- raggiungibilita' del Nest Hub;
- servizio Google AI TTS;
- impostazione del volume;
- muting temporaneo della TV, se abilitato e applicabile;
- ripristino della TV al termine del messaggio.

Durante il test dovresti sentire un messaggio simile a:

```text
Echo Home e' attivo. Test vocale completato.
```

## Cosa non simula il pulsante

Il pulsante verifica il percorso audio, ma non simula un vero rientro.

Non modifica artificialmente:

- lo stato di `person.stefano` o `person.laura`;
- lo stato del sensore del portone;
- la combinazione temporale tra presenza e portone;
- il promemoria dell'asciugatrice.

Per verificare completamente la logica di arrivo e' necessario un vero passaggio `not_home → home` abbinato all'apertura del portone entro la finestra prevista.

## Risoluzione dei problemi

### La card mostra un'entita' non disponibile

Controlla che l'entity ID indicato nella card corrisponda a quello realmente presente in Home Assistant.

Verifica le entita' da:

**Strumenti per sviluppatori → Stati**

### Il pulsante non produce alcun messaggio

Controlla, nell'ordine:

1. che `input_button.echo_home_test_vocale` esista;
2. che l'automazione Eco Home sia attiva;
3. che `media_player.nest_hub_sala` sia disponibile;
4. che `tts.google_ai_tts` sia configurato;
5. la traccia dell'ultima esecuzione dell'automazione.

### La TV non viene silenziata

Il muting viene eseguito soltanto se:

- la funzione TV ducking e' abilitata nell'automazione;
- il media player della TV e' disponibile;
- la TV non e' spenta, in standby, sconosciuta o non disponibile;
- la TV non era gia' silenziata.

### Il test parla ma il rientro reale non funziona

In questo caso TTS e Nest Hub funzionano. Il problema e' probabilmente nella conferma del rientro.

Controlla nella traccia:

```text
person_arrived_recently
door_opened_recently
trigger_person_arrival_valid
trigger_door_open_valid
arrival_confirmed_by_person_and_door
```

Nella versione 1.1.2 il rientro puo' essere confermato in entrambi gli ordini:

```text
persona home → portone
portone → persona home
```

I due eventi devono comunque verificarsi entro la finestra temporale configurata.

## Rimozione della card

La rimozione della card non elimina Eco Home e non modifica gli helper.

Per rimuoverla:

1. apri **Modifica plancia**;
2. seleziona la card Eco Home;
3. premi **Elimina scheda**;
4. conferma e salva la plancia.

