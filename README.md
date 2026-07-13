<div align="center">

# Eco Home

**Benvenuto intelligente per Home Assistant, confermato da presenza e apertura del portone.**

[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-Automation-41BDF5?style=flat-square&logo=homeassistant&logoColor=white)](https://www.home-assistant.io/)
[![Versione](https://img.shields.io/badge/versione-1.1.2-2ea44f?style=flat-square)](eco-home-v1.1.2.yaml)
[![Formato](https://img.shields.io/badge/formato-YAML-CB171E?style=flat-square&logo=yaml&logoColor=white)](eco-home-v1.1.2.yaml)

</div>

## Cos'è Eco Home

Eco Home è un'automazione YAML per Home Assistant che riproduce un messaggio personalizzato sul Nest Hub quando un rientro viene confermato dalla presenza di una persona tracciata e dall'apertura del portone.

Le frasi vengono scelte localmente da raccolte integrate nell'automazione. Google AI TTS viene usato esclusivamente per la sintesi vocale.

## Novità della versione 1.1.2

La combinazione presenza-portone funziona ora in entrambi gli ordini:

```text
persona home → apertura portone
apertura portone → persona home
```

I due eventi devono verificarsi entro la finestra configurata, pari a 5 minuti per impostazione predefinita. In questo modo il messaggio non viene perso quando GPS o Wi-Fi aggiornano la presenza dopo l'apertura del portone.

Il riconoscimento usa gli entity ID `person.stefano` e `person.laura`, non il nome completo dell'entità. Il TTS sceglie quindi un nomignolo casuale maschile, femminile o di coppia.

Consulta il [changelog](CHANGELOG.md) per l'elenco completo delle modifiche.

## Funzioni incluse

- riconoscimento bidirezionale tra presenza e portone;
- saluti e nomignoli casuali per Stefano, Laura o entrambi;
- frasi variabili in base a persona, fascia oraria, fine settimana e ricorrenze;
- accensione della luce ambiente solo quando fuori è buio;
- volume del Nest Hub differenziato tra giorno e notte;
- silenziamento temporaneo della TV durante il messaggio;
- promemoria dell'asciugatrice terminata durante l'assenza;
- pulsante di test vocale manuale;
- card Lovelace opzionale;
- Logbook diagnostico quando `debug: true`;
- protezione dagli annunci duplicati.

## Requisiti principali

| Funzione | Entità di esempio | Necessaria |
|---|---|---:|
| Persone tracciate | `person.stefano`, `person.laura` | Sì |
| Sensore del portone | `binary_sensor.porta_contact` | Sì |
| Altoparlante | `media_player.nest_hub_sala` | Sì |
| Motore vocale | `tts.google_ai_tts` | Sì |
| Luce ambiente | `light.luceambiente` | Opzionale |
| TV | `media_player.tv_sala_ue85du7170uxzt` | Opzionale |
| Stato asciugatrice | `sensor.esterno_asciugatrice_machine_state` | Opzionale |
| Fine asciugatrice | `sensor.esterno_asciugatrice_completion_time` | Opzionale |

Gli entity ID sono esempi e devono essere adattati alla propria installazione. Consulta [DIPENDENZE.md](DIPENDENZE.md) e [GUIDA_PERSONALIZZAZIONE.md](GUIDA_PERSONALIZZAZIONE.md).

## Helper richiesti

```text
input_boolean.echo_home_attivo
input_boolean.echo_home_silenzioso
input_boolean.echo_home_asciugatrice_da_annunciare
input_datetime.echo_home_asciugatrice_fine
input_datetime.echo_home_ultimo_annuncio
input_button.echo_home_test_vocale
```

La versione 1.1.2 non richiede nuovi helper rispetto alla 1.1.1.

## Installazione

1. Leggi [DIPENDENZE.md](DIPENDENZE.md).
2. Scarica [eco-home-v1.1.2.yaml](eco-home-v1.1.2.yaml).
3. Copia l'intero blocco alla fine di `/config/automations.yaml`, oppure sostituisci solamente la precedente automazione Eco Home.
4. Non sostituire l'intero `automations.yaml` se contiene altre automazioni.
5. Adatta gli entity ID seguendo [GUIDA_PERSONALIZZAZIONE.md](GUIDA_PERSONALIZZAZIONE.md).
6. Da Home Assistant esegui **Controlla configurazione**.
7. Ricarica le automazioni e usa il pulsante di test vocale.

Stai usando la 1.1.1? Segui la [guida di aggiornamento alla 1.1.2](GUIDA_AGGIORNAMENTO.md) per conservare tutte le altre automazioni.

Con la configurazione standard, `configuration.yaml` contiene:

```yaml
automation: !include automations.yaml
```

## Card Lovelace opzionale

File disponibili:

- [eco-home-v1.1.2-dashboard-card.yaml](eco-home-v1.1.2-dashboard-card.yaml)
- [GUIDA_CARD_TEST.md](GUIDA_CARD_TEST.md)

La card usa soltanto componenti standard di Home Assistant e non richiede HACS.

## Struttura del repository

| File | Contenuto |
|---|---|
| [eco-home-v1.1.2.yaml](eco-home-v1.1.2.yaml) | Automazione standalone |
| [CHANGELOG.md](CHANGELOG.md) | Cronologia delle versioni |
| [DIPENDENZE.md](DIPENDENZE.md) | Entità, integrazioni e helper richiesti |
| [GUIDA_AGGIORNAMENTO.md](GUIDA_AGGIORNAMENTO.md) | Aggiornamento dalla 1.1.1 alla 1.1.2 senza perdere altre automazioni |
| [GUIDA_PERSONALIZZAZIONE.md](GUIDA_PERSONALIZZAZIONE.md) | Personalizzazione dell'automazione |
| [GUIDA_PULSANTE_TEST.md](GUIDA_PULSANTE_TEST.md) | Utilizzo del test vocale |
| [eco-home-v1.1.2-dashboard-card.yaml](eco-home-v1.1.2-dashboard-card.yaml) | Card Lovelace |
| [GUIDA_CARD_TEST.md](GUIDA_CARD_TEST.md) | Installazione e utilizzo della card |
| [archive/v1.1.1](archive/v1.1.1) | File archiviati della versione 1.1.1 |

## Versioni archiviate

I file delle versioni precedenti sono conservati nella cartella [`archive`](archive) e non sono mescolati con quelli della versione corrente.

- [Eco Home v1.1.1](archive/v1.1.1)

Per una nuova installazione utilizza sempre i file `v1.1.2` presenti nella cartella principale.

## Risoluzione rapida

Se il test vocale funziona ma il rientro no, controlla nella traccia:

```text
door_opened_recently
person_arrived_recently
trigger_person_arrival_valid
trigger_door_open_valid
arrival_confirmed_by_person_and_door
```

Verifica inoltre lo stato usato dal sensore del portone. La configurazione predefinita considera `on` come aperto.

## Supporto

Per problemi tecnici o suggerimenti utilizza la sezione [Issues](https://github.com/gates538/eco-home/issues).

Il progetto è disponibile gratuitamente. Se vuoi sostenerlo:

[![Sostieni Eco Home su GitHub Sponsors](https://img.shields.io/badge/GitHub%20Sponsors-Sostieni%20Eco%20Home-EA4AAA?style=for-the-badge&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/gates538)
