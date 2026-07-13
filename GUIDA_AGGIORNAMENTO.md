# Guida aggiornamento Eco Home

Questa guida spiega come aggiornare **Eco Home dalla versione 1.1.1 alla 1.1.2** senza perdere le altre automazioni presenti in Home Assistant.

## Prima di iniziare

La versione 1.1.2:

- non richiede nuovi helper;
- non richiede nuove entità;
- mantiene la compatibilità con la configurazione della 1.1.1;
- corregge il rientro quando il portone viene aperto prima che la persona risulti `home`;
- usa nomignoli casuali per Stefano, Laura o la coppia.

## 1. Crea una copia di sicurezza

Prima di modificare i file:

1. apri **Impostazioni → Sistema → Backup**;
2. crea un nuovo backup;
3. in alternativa, copia almeno `/config/automations.yaml` in un posto sicuro.

## 2. Scarica la nuova automazione

Scarica il file:

- [eco-home-v1.1.2.yaml](eco-home-v1.1.2.yaml)

Non copiare il file della cartella `archive/v1.1.1`: serve soltanto come archivio della versione precedente.

## 3. Aggiorna senza cancellare le altre automazioni

Il file `automations.yaml` può contenere molte automazioni. **Non sostituire l'intero file** con `eco-home-v1.1.2.yaml`.

Apri `/config/automations.yaml` con File editor, Studio Code Server o Samba e cerca il blocco che inizia con:

```yaml
- id: '1783777716602'
  alias: Eco home
```

Elimina solamente l'intero blocco dell'automazione **Eco home**, fino alla riga precedente all'automazione successiva.

Al suo posto incolla tutto il contenuto di `eco-home-v1.1.2.yaml`.

Le altre automazioni presenti prima e dopo quel blocco devono restare invariate.

> Se il tuo ID è diverso, cerca `alias: Eco home` e sostituisci il relativo blocco completo.

## 4. Controlla le entità personalizzate

Se nella versione 1.1.1 avevi modificato entity ID, tempi o volumi, confrontali con la nuova versione.

Controlla in particolare:

```text
person.stefano
person.laura
binary_sensor.porta_contact
media_player.nest_hub_sala
tts.google_ai_tts
```

Per l'elenco completo consulta:

- [GUIDA_PERSONALIZZAZIONE.md](GUIDA_PERSONALIZZAZIONE.md)
- [DIPENDENZE.md](DIPENDENZE.md)

Non copiare automaticamente il vecchio codice sopra la nuova versione: riporta soltanto i tuoi entity ID e le impostazioni personalizzate.

## 5. Salva e verifica la configurazione

Dopo aver salvato `automations.yaml`:

1. apri **Strumenti per sviluppatori → YAML**;
2. esegui **Controlla configurazione**;
3. se il controllo non segnala errori, seleziona **Ricarica automazioni**;
4. se Home Assistant richiede il riavvio, eseguilo solo dopo un controllo valido.

Se compare un errore YAML, ripristina il backup del file e verifica soprattutto:

- il trattino `-` iniziale dell'automazione;
- l'indentazione;
- che non sia rimasta una parte della vecchia automazione;
- che l'automazione successiva inizi ancora con il proprio trattino.

## 6. Esegui il test vocale

Usa:

```text
input_button.echo_home_test_vocale
```

oppure installa la card:

- [eco-home-v1.1.2-dashboard-card.yaml](eco-home-v1.1.2-dashboard-card.yaml)
- [GUIDA_CARD_TEST.md](GUIDA_CARD_TEST.md)

Il test vocale verifica Nest Hub, volume, TTS e silenziamento temporaneo della TV. Non simula la combinazione reale tra presenza e portone.

## 7. Verifica un rientro reale

La versione 1.1.2 accetta entrambi gli ordini:

```text
persona home → apertura portone
apertura portone → persona home
```

I due eventi devono avvenire entro 5 minuti. Dopo la conferma, il messaggio parte con un breve ritardo.

Se non funziona, abilita temporaneamente `debug: true` nell'automazione e controlla la traccia o il Logbook. Le variabili più utili sono:

```text
door_opened_recently
person_arrived_recently
trigger_person_arrival_valid
trigger_door_open_valid
arrival_confirmed_by_person_and_door
```

## Ripristino della versione precedente

Se devi tornare alla 1.1.1:

1. apri [archive/v1.1.1](archive/v1.1.1);
2. scarica `eco-home-v1.1.1.yaml`;
3. sostituisci solamente il blocco `alias: Eco home` in `automations.yaml`;
4. controlla la configurazione e ricarica le automazioni.

La 1.1.1 resta archiviata per emergenza, ma per l'uso normale è consigliata la 1.1.2.
