<div align="center">

# Eco Home

**Benvenuto intelligente per Home Assistant, confermato da presenza e apertura del portone.**

[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-Automation-41BDF5?style=flat-square&logo=homeassistant&logoColor=white)](https://www.home-assistant.io/)
[![Versione](https://img.shields.io/badge/versione-1.1.8-2ea44f?style=flat-square)](eco-home-v1.1.8.yaml)
[![Formato](https://img.shields.io/badge/formato-YAML-CB171E?style=flat-square&logo=yaml&logoColor=white)](eco-home-v1.1.8.yaml)

</div>

## Novità della versione 1.1.8

- **Lettura Temperatura Interna**: l'altoparlante annuncia all'arrivo la temperatura media interna della casa (es: *"In casa ci sono 24,5 gradi"*).
- **Accensione Condizionatori**: se la temperatura interna supera i 26°C, l'automazione invia una notifica push interattiva chiedendo se desideri accendere l'aria condizionata. Cliccando su "Sì, accendi", i condizionatori configurati si avviano in modalità raffrescamento (`cool`).
- **Configurazione Clima**: nuove variabili globali per indicare la lista di sensori di temperatura e i condizionatori da gestire.

<details>
<summary>Novità delle versioni precedenti</summary>

### Novità della versione 1.1.8
- **Rimozione ritardo iniziale**: rimosso il ritardo fisso di 3 secondi prima dell'annuncio vocale (`arrival_group_window_seconds: 0`);
- **Aggiornamento documentazione**: riallineati tutti i riferimenti e i numeri di riga delle guide alla personalizzazione e all'aggiornamento.

### Novità della versione 1.1.8
- **Notifiche Push con Foto**: scatto di uno snapshot (tramite telecamera compatibile, es. `camera.sala_2`) e invio push con immagine allegata al rientro dei residenti;
- **Controllo Sicurezza Presenza**: lo snapshot e la notifica con immagine vengono inviati **solo se la casa era completamente vuota** prima del rientro rilevato (evitando notifiche superflue se ci sono già persone in casa);
- **Controllo tramite Card**: aggiunto il nuovo helper `input_boolean.eco_home_notifiche_foto` per disattivare/attivare le notifiche con foto direttamente dalla dashboard;
- **Servizi di Notifica Personalizzati**: variabili configurabili nell'automazione per associare le notifiche push ai singoli cellulari (es. `notify.mobile_app_stefano`);
- Aggiornati tutti i file di configurazione, card e documentazione alla release 1.1.8.

</details>

La logica di rientro principale continua a funzionare in entrambi gli ordini:

```text
persona home → apertura portone
apertura portone → persona home
```

## Funzioni principali

- conferma presenza-portone entro 5 minuti;
- saluti e nomignoli casuali per Stefano, Laura o entrambi;
- notifiche push ricche con foto sul telefono al rientro (solo se la casa era vuota);
- messaggi diversi per giorno, sera, notte, fine settimana e ricorrenze;
- accensione della luce ambiente soltanto quando fuori è buio;
- volume differenziato per fascia oraria e successivo ripristino;
- silenziamento temporaneo della TV senza alterare un mute già presente;
- promemoria dell'asciugatrice terminata durante l'assenza;
- test vocale per scenario;
- diagnostica consultabile dalla card e dal Logbook;
- protezione dagli annunci duplicati.

## Installazione nuova

1. Controlla i dispositivi necessari in [REQUISITI_HARDWARE.md](REQUISITI_HARDWARE.md).
2. Leggi l'elenco di entità e helper in [DIPENDENZE.md](DIPENDENZE.md).
3. Installa [eco-home-v1.1.8-helpers.yaml](eco-home-v1.1.8-helpers.yaml) come package oppure segui [GUIDA_HELPER_UI.md](GUIDA_HELPER_UI.md).
4. Copia [eco-home-v1.1.8.yaml](eco-home-v1.1.8.yaml) in `automations.yaml`.
5. Non sostituire l'intero `automations.yaml` se contiene altre automazioni.
6. Adatta gli entity ID seguendo [GUIDA_PERSONALIZZAZIONE.md](GUIDA_PERSONALIZZAZIONE.md).
7. Esegui **Controlla configurazione** e poi **Ricarica automazioni**.
8. Installa la card seguendo [GUIDA_CARD_TEST.md](GUIDA_CARD_TEST.md).

## Aggiornamento dalla 1.1.8 o precedente

Segui [GUIDA_AGGIORNAMENTO.md](GUIDA_AGGIORNAMENTO.md). Prima di installare l'automazione devi creare la cartella per gli snapshot locali ed aggiungere il nuovo helper `input_boolean.eco_home_notifiche_foto`.

## File della versione corrente

| File | Contenuto |
|---|---|
| [eco-home-v1.1.8.yaml](eco-home-v1.1.8.yaml) | Automazione standalone |
| [eco-home-v1.1.8-dashboard-card.yaml](eco-home-v1.1.8-dashboard-card.yaml) | Card Lovelace completa |
| [eco-home-v1.1.8-helpers.yaml](eco-home-v1.1.8-helpers.yaml) | Package completo degli helper |
| [eco-home-v1.1.8-dashboard-tuttacasa.yaml](eco-home-v1.1.8-dashboard-tuttacasa.yaml) | Plancia completa "Tutta Casa" |
| [DIPENDENZE.md](DIPENDENZE.md) | Entità e integrazioni richieste |
| [REQUISITI_HARDWARE.md](REQUISITI_HARDWARE.md) | Hardware necessario, esempi e prove di compatibilità |
| [GUIDA_HELPER_UI.md](GUIDA_HELPER_UI.md) | Creazione o verifica dei 15 helper dalla UI |
| [GUIDA_PERSONALIZZAZIONE.md](GUIDA_PERSONALIZZAZIONE.md) | Entity ID e impostazioni da adattare |
| [GUIDA_PULSANTE_TEST.md](GUIDA_PULSANTE_TEST.md) | Scenari del test vocale |
| [GUIDA_CARD_TEST.md](GUIDA_CARD_TEST.md) | Installazione e utilizzo della card |
| [GUIDA_AGGIORNAMENTO.md](GUIDA_AGGIORNAMENTO.md) | Procedura di migrazione e setup degli snapshot |
| [GUIDA_DIAGNOSTICA.md](GUIDA_DIAGNOSTICA.md) | Interpretazione degli esiti diagnostici |
| [CHANGELOG.md](CHANGELOG.md) | Cronologia delle versioni |

## Versioni archiviate

Le versioni precedenti restano nella cartella [`archive`](archive):

- [Eco Home v1.1.8](archive/v1.1.8)
- [Eco Home v1.1.8](archive/v1.1.8)
- [Eco Home v1.1.8](archive/v1.1.8)
- [Eco Home v1.1.3](archive/v1.1.3)
- [Eco Home v1.1.2](archive/v1.1.2)
- [Eco Home v1.1.1](archive/v1.1.1)

Per nuove installazioni usa sempre i file `v1.1.8` nella cartella principale.

## Supporto

Per problemi o suggerimenti utilizza le [Issues](https://github.com/gates538/eco-home/issues).

[![Sostieni Eco Home su GitHub Sponsors](https://img.shields.io/badge/GitHub%20Sponsors-Sostieni%20Eco%20Home-EA4AAA?style=for-the-badge&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/gates538)

