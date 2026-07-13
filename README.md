<div align="center">

# Eco Home

**Benvenuto intelligente per Home Assistant, confermato da presenza e apertura del portone.**

[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-Automation-41BDF5?style=flat-square&logo=homeassistant&logoColor=white)](https://www.home-assistant.io/)
[![Versione](https://img.shields.io/badge/versione-1.1.3-2ea44f?style=flat-square)](eco-home-v1.1.3.yaml)
[![Formato](https://img.shields.io/badge/formato-YAML-CB171E?style=flat-square&logo=yaml&logoColor=white)](eco-home-v1.1.3.yaml)

</div>

## Novità della versione 1.1.3

- sei scenari selezionabili dalla card: percorso audio, Stefano, Laura, coppia, notte e asciugatrice;
- ripristino automatico del volume precedente del Nest Hub dopo TTS;
- diagnostica persistente con ultimo evento, esito, persona, profilo e messaggio;
- card ampliata con persone, portone, asciugatrice e stato del Nest Hub;
- protezione esplicita dalle transizioni provenienti da `unknown` e `unavailable`;
- gestione pulita del Nest Hub non disponibile, senza perdere la diagnostica;
- file helper completo e file di aggiornamento dedicato a chi proviene dalla 1.1.2.

La logica di rientro continua a funzionare in entrambi gli ordini:

```text
persona home → apertura portone
apertura portone → persona home
```

## Funzioni principali

- conferma presenza-portone entro 5 minuti;
- saluti e nomignoli casuali per Stefano, Laura o entrambi;
- messaggi diversi per giorno, sera, notte, fine settimana e ricorrenze;
- accensione della luce ambiente soltanto quando fuori è buio;
- volume differenziato per fascia oraria e successivo ripristino;
- silenziamento temporaneo della TV senza alterare un mute già presente;
- promemoria dell'asciugatrice terminata durante l'assenza;
- test vocale per scenario;
- diagnostica consultabile dalla card e dal Logbook;
- protezione dagli annunci duplicati.

## Installazione nuova

1. Leggi [DIPENDENZE.md](DIPENDENZE.md).
2. Installa [eco-home-v1.1.3-helpers.yaml](eco-home-v1.1.3-helpers.yaml) come package oppure crea gli stessi helper dalla UI.
3. Copia [eco-home-v1.1.3.yaml](eco-home-v1.1.3.yaml) in `automations.yaml`.
4. Non sostituire l'intero `automations.yaml` se contiene altre automazioni.
5. Adatta gli entity ID seguendo [GUIDA_PERSONALIZZAZIONE.md](GUIDA_PERSONALIZZAZIONE.md).
6. Esegui **Controlla configurazione** e poi **Ricarica automazioni**.
7. Installa la card seguendo [GUIDA_CARD_TEST.md](GUIDA_CARD_TEST.md).

## Aggiornamento dalla 1.1.2

Segui [GUIDA_AGGIORNAMENTO.md](GUIDA_AGGIORNAMENTO.md). Il file
[eco-home-v1.1.3-helper-update.yaml](eco-home-v1.1.3-helper-update.yaml)
contiene soltanto i nuovi helper della 1.1.3.

## File della versione corrente

| File | Contenuto |
|---|---|
| [eco-home-v1.1.3.yaml](eco-home-v1.1.3.yaml) | Automazione standalone |
| [eco-home-v1.1.3-dashboard-card.yaml](eco-home-v1.1.3-dashboard-card.yaml) | Card Lovelace completa |
| [eco-home-v1.1.3-helpers.yaml](eco-home-v1.1.3-helpers.yaml) | Package completo degli helper |
| [eco-home-v1.1.3-helper-update.yaml](eco-home-v1.1.3-helper-update.yaml) | Solo helper nuovi per aggiornare dalla 1.1.2 |
| [DIPENDENZE.md](DIPENDENZE.md) | Entità e integrazioni richieste |
| [GUIDA_PERSONALIZZAZIONE.md](GUIDA_PERSONALIZZAZIONE.md) | Entity ID e impostazioni da adattare |
| [GUIDA_PULSANTE_TEST.md](GUIDA_PULSANTE_TEST.md) | Scenari del test vocale |
| [GUIDA_CARD_TEST.md](GUIDA_CARD_TEST.md) | Installazione e utilizzo della card |
| [GUIDA_AGGIORNAMENTO.md](GUIDA_AGGIORNAMENTO.md) | Passaggio sicuro dalla 1.1.2 |
| [GUIDA_DIAGNOSTICA.md](GUIDA_DIAGNOSTICA.md) | Interpretazione degli esiti diagnostici |
| [CHANGELOG.md](CHANGELOG.md) | Cronologia delle versioni |

## Versioni archiviate

Le versioni precedenti restano nella cartella [`archive`](archive):

- [Eco Home v1.1.2](archive/v1.1.2)
- [Eco Home v1.1.1](archive/v1.1.1)

Per nuove installazioni usa sempre i file `v1.1.3` nella cartella principale.

## Supporto

Per problemi o suggerimenti utilizza le [Issues](https://github.com/gates538/eco-home/issues).

[![Sostieni Eco Home su GitHub Sponsors](https://img.shields.io/badge/GitHub%20Sponsors-Sostieni%20Eco%20Home-EA4AAA?style=for-the-badge&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/gates538)

