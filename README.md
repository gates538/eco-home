<div align="center">

# Eco Home

**Benvenuto intelligente per Home Assistant, confermato da presenza e apertura del portone.**

[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-Automation-41BDF5?style=flat-square&logo=homeassistant&logoColor=white)](https://www.home-assistant.io/)
[![Versione](https://img.shields.io/badge/versione-1.1.1-2ea44f?style=flat-square)](eco-home-v1.1.1.yaml)
[![Formato](https://img.shields.io/badge/formato-YAML-CB171E?style=flat-square&logo=yaml&logoColor=white)](eco-home-v1.1.1.yaml)
[![Dipendenze](https://img.shields.io/badge/dipendenze-documentate-blue?style=flat-square)](DIPENDENZE.md)

</div>

## Cos'è Eco Home

Eco Home è un'automazione YAML per Home Assistant che riproduce un messaggio personalizzato sul Nest Hub quando un rientro viene confermato dalla presenza di una persona tracciata e dall'apertura del portone.

Il progetto non genera le frasi tramite servizi AI esterni: i messaggi sono scelti localmente da raccolte integrate nell'automazione. Il motore Google AI TTS viene utilizzato esclusivamente per la sintesi vocale.

## Come funziona la versione 1.1.1

1. Una persona configurata passa allo stato `home`.
2. Il portone viene aperto entro i successivi 5 minuti.
3. Eco Home attende 3 secondi per raggruppare eventuali arrivi ravvicinati.
4. Il messaggio viene riprodotto sul Nest Hub.

> [!IMPORTANT]
> Nella versione `1.1.1` il messaggio di benvenuto viene eseguito dal trigger del portone. L'ordine operativo supportato è quindi **persona rilevata a casa → apertura del portone entro 5 minuti**. L'apertura del portone seguita successivamente dall'arrivo della persona non avvia il messaggio in questa versione.

## Funzioni incluse

- saluto personalizzato per Stefano, Laura o entrambi;
- frasi variabili in base a persona, fascia oraria, fine settimana, festività e date personali;
- accensione immediata della luce ambiente solo quando `sun.sun` è sotto l'orizzonte e la luce è spenta;
- luce impostata al 45% e a 4000 K;
- volume del Nest Hub all'80% tra le 06:00 e le 23:00 e al 40% tra le 23:00 e le 06:00;
- silenziamento temporaneo della TV durante il messaggio, escluso l'orario notturno;
- ripristino automatico dell'audio della TV dopo la sintesi vocale;
- promemoria se l'asciugatrice termina mentre non è presente nessuno;
- validità del promemoria asciugatrice per 12 ore;
- indicazione del tempo residuo dell'asciugatrice quando il dato è disponibile;
- pulsante per il test vocale manuale;
- registrazione di informazioni diagnostiche nel Logbook quando il debug è attivo;
- protezione dagli annunci duplicati mediante un breve tempo di attesa tra le esecuzioni.

## Requisiti principali

| Funzione | Entità configurata | Necessaria |
|---|---|---:|
| Persone tracciate | `person.stefano`, `person.laura` | Sì |
| Sensore del portone | `binary_sensor.porta_contact` | Sì |
| Altoparlante | `media_player.nest_hub_sala` | Sì |
| Motore vocale | `tts.google_ai_tts` | Sì |
| Integrazione solare | `sun.sun` | Sì, per la luce |
| Luce ambiente | `light.luceambiente` | Solo per l'accensione automatica |
| TV | `media_player.tv_sala_ue85du7170uxzt` | Solo per il muting temporaneo |
| Stato asciugatrice | `sensor.esterno_asciugatrice_machine_state` | Solo per il promemoria |
| Fine prevista asciugatrice | `sensor.esterno_asciugatrice_completion_time` | Solo per il tempo residuo |

Gli entity ID sono esempi della configurazione originale e devono essere sostituiti con quelli presenti nella propria installazione.

La guida completa è disponibile in **[DIPENDENZE.md](DIPENDENZE.md)**.

## Helper richiesti

L'automazione utilizza questi helper:

```text
input_boolean.echo_home_attivo
input_boolean.echo_home_silenzioso
input_boolean.echo_home_asciugatrice_da_annunciare
input_datetime.echo_home_asciugatrice_fine
input_datetime.echo_home_ultimo_annuncio
input_button.echo_home_test_vocale
```

Possono essere creati dalla UI di Home Assistant oppure tramite il package YAML riportato in [DIPENDENZE.md](DIPENDENZE.md#helper-richiesti).

## Installazione

### 1. Verifica le dipendenze

Leggi [DIPENDENZE.md](DIPENDENZE.md) e controlla che integrazioni, dispositivi ed helper siano disponibili.

### 2. Installa gli helper

Creali dalla UI di Home Assistant oppure usa il blocco package presente nella guida delle dipendenze.

Per caricare i package, `configuration.yaml` deve contenere:

```yaml
homeassistant:
  packages: !include_dir_named packages
```

### 3. Installa l'automazione

Il file [eco-home-v1.1.1.yaml](eco-home-v1.1.1.yaml) è già nel formato elenco usato da `automations.yaml`.

Con la configurazione standard:

```yaml
automation: !include automations.yaml
```

copia l'intero contenuto del file alla fine di `automations.yaml`, mantenendo il trattino iniziale dell'automazione.

### 4. Personalizza gli entity ID

Aggiorna almeno:

```text
person.stefano
person.laura
binary_sensor.porta_contact
media_player.nest_hub_sala
tts.google_ai_tts
```

Poi configura, se utilizzate, luce, TV e asciugatrice.

Consulta [GUIDA_PERSONALIZZAZIONE.md](GUIDA_PERSONALIZZAZIONE.md) come riferimento per individuare le sezioni principali da modificare.

### 5. Controlla la configurazione

Da Home Assistant:

1. apri **Strumenti per sviluppatori → YAML**;
2. esegui **Controlla configurazione**;
3. se non vengono rilevati errori, ricarica le automazioni oppure riavvia Home Assistant;
4. premi `input_button.echo_home_test_vocale` per verificare Nest Hub, TTS, volume e muting della TV.

## Sensore del portone

La configurazione predefinita considera il portone aperto quando il sensore passa a `on`:

```yaml
to: "on"
```

Se il sensore utilizza `off` per indicare l'apertura, modifica sia il trigger sia il controllo `trigger_to_state` collegato alla conferma del rientro. Cambiare soltanto il trigger non è sufficiente.

## Card Lovelace opzionale

La card consente di:

- attivare o disattivare Eco Home;
- abilitare la modalità silenziosa;
- verificare il promemoria dell'asciugatrice;
- visualizzare l'ultimo annuncio;
- eseguire il test vocale.

File da utilizzare:

- [eco-home-v1.1.1-dashboard-card.yaml](eco-home-v1.1.1-dashboard-card.yaml)
- [GUIDA_CARD_TEST.md](GUIDA_CARD_TEST.md)

La card utilizza soltanto componenti standard di Home Assistant e non richiede HACS.

## Struttura del repository

| File | Contenuto |
|---|---|
| [eco-home-v1.1.1.yaml](eco-home-v1.1.1.yaml) | Automazione completa |
| [DIPENDENZE.md](DIPENDENZE.md) | Integrazioni, entità, helper e servizi richiesti |
| [GUIDA_PERSONALIZZAZIONE.md](GUIDA_PERSONALIZZAZIONE.md) | Riferimento per adattare gli entity ID e le impostazioni |
| [GUIDA_PULSANTE_TEST.md](GUIDA_PULSANTE_TEST.md) | Configurazione e utilizzo del test vocale |
| [eco-home-v1.1.1-dashboard-card.yaml](eco-home-v1.1.1-dashboard-card.yaml) | Card Lovelace di controllo |
| [GUIDA_CARD_TEST.md](GUIDA_CARD_TEST.md) | Installazione e utilizzo della card |

## Cosa non è richiesto

- HACS;
- componenti personalizzati;
- `requirements.txt`;
- librerie Python aggiuntive;
- `package.json`;
- servizi AI esterni per generare i messaggi.

## Risoluzione rapida dei problemi

### Il test vocale funziona, ma il rientro no

Controlla:

- che la persona passi realmente da uno stato diverso da `home` a `home`;
- che il portone venga aperto entro 5 minuti dal cambio di presenza;
- che il sensore del portone utilizzi lo stato configurato;
- che Eco Home sia attivo e non in modalità silenziosa;
- la traccia dell'ultima esecuzione dell'automazione.

### La luce non si accende

La luce viene accesa soltanto quando:

- `sun.sun` è `below_horizon`;
- `light.luceambiente` è `off`;
- l'entity ID è corretto e disponibile.

### La TV non viene silenziata

Il muting viene ignorato se:

- è notte;
- la funzione è disabilitata;
- la TV è spenta, in standby, `unknown` o `unavailable`;
- la TV era già silenziata.

## Supporto al progetto

Eco Home viene condiviso gratuitamente. Una sponsorizzazione è facoltativa, ma aiuta a dedicare tempo a manutenzione, documentazione e nuove funzioni.

<div align="center">

[![Sostieni Eco Home su GitHub Sponsors](https://img.shields.io/badge/GitHub%20Sponsors-Sostieni%20Eco%20Home-EA4AAA?style=for-the-badge&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/gates538)

</div>

Il progetto rimane utilizzabile anche senza alcun contributo economico.

Per problemi tecnici o suggerimenti, utilizza la sezione [Issues](https://github.com/gates538/eco-home/issues) del repository.
