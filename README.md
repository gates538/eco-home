<div align="center">

# Eco Home

**Benvenuto intelligente e domotica vocale per Home Assistant, confermato da presenza e apertura del portone.**

[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-Automation-41BDF5?style=flat-square&logo=homeassistant&logoColor=white)](https://www.home-assistant.io/)
[![Versione](https://img.shields.io/badge/versione-1.5.0-2ea44f?style=flat-square)](CHANGELOG.md)
[![Formato](https://img.shields.io/badge/formato-YAML-CB171E?style=flat-square&logo=yaml&logoColor=white)](CHANGELOG.md)

</div>

## Novità della versione 1.5.0

- **Riorganizzazione Modulare**: Architettura pulita e divisa in cartelle logiche (`/automations`, `/docs`, `/scripts`, `/archive`).
- **Fix Race Condition su Rientri di Coppia**: Modalità `queued` (`max: 10`) nel modulo principale per eliminare accavallamenti e mutismo su Google Nest Hub.
- **Voce Femminile Vivace & Naturale**: Uniformate tutte le 16 chiamate TTS su `tts.google_translate_it_lt` con `language: "it"` e `options: { tld: "it" }`.
- **Personalizzazione Sartoriale Routine**: Riconoscimento pausa pranzo, rientri scaglionati di Stefano e Laura, citazioni simpatiche per le micie Piccola e Luna (e Luna nel lavandino!), riscaldamento con termocamino a pellet / climatizzatore sala 18.000 BTU e dual-split.
- **Allerte Sarcastiche Esparse**: Nuove varianti spiritose per frigo/freezer aperti, vento forte in terrazza, pioggia, cottura dimenticata (>60 min), asciugatrice e dispenser pappa.
- **Sicurezza e Privacy**: Sanitizzazione completa dei repository con esclusione di credenziali e file temporanei tramite `.gitignore`.

---

## Struttura del Progetto

- **`/automations`**: Contiene tutti i moduli YAML (`eco-home-v1.5.0-*.yaml`, `luci.yaml`, `notifiche.yaml`).
- **`/docs`**: Contiene guide, documentazione di configurazione e requisiti.
- **`/scripts`**: Contiene script di utilità e automazione locale.
- **`/archive`**: Raccolta delle release storiche precedenti.

---

## File della versione corrente

| File | Contenuto |
|---|---|
| [automations/eco-home-v1.5.0-core.yaml](automations/eco-home-v1.5.0-core.yaml) | Modulo Core principale (Presenza, Portone, Saluto Vocale Nest Hub) |
| [automations/eco-home-v1.5.0-cucina.yaml](automations/eco-home-v1.5.0-cucina.yaml) | Modulo Cucina & Annunci avvio cottura |
| [automations/eco-home-v1.5.0-climate.yaml](automations/eco-home-v1.5.0-climate.yaml) | Modulo Clima & Risparmio Energetico Finestre |
| [automations/eco-home-v1.5.0-frigo-meteo-asciugatrice.yaml](automations/eco-home-v1.5.0-frigo-meteo-asciugatrice.yaml) | Allerte Frigo, Freezer, Vento in Terrazza & Asciugatrice |
| [automations/eco-home-v1.5.0-pets-and-car.yaml](automations/eco-home-v1.5.0-pets-and-car.yaml) | Modulo Animali (Piccola & Luna) e Promemoria Auto (Discovery) |
| [automations/eco-home-v1.5.0-security.yaml](automations/eco-home-v1.5.0-security.yaml) | Modulo Guardiano Uscite & Allarme Intrusione |
| [automations/eco-home-v1.5.0-cottura-dimenticata.yaml](automations/eco-home-v1.5.0-cottura-dimenticata.yaml) | Allerta fornelli/forno accesi oltre 60 minuti |
| [automations/eco-home-v1.5.0-dobby-and-frost.yaml](automations/eco-home-v1.5.0-dobby-and-frost.yaml) | Modulo Robot Dobby & Allerta Gelo Notturno Auto |
| [automations/eco-home-v1.5.0-emby-cinema-silenzioso.yaml](automations/eco-home-v1.5.0-emby-cinema-silenzioso.yaml) | Modalità Silenziosa automatica durante Film Emby/TV |
| [automations/eco-home-v1.5.0-zero-sprechi-luci.yaml](automations/eco-home-v1.5.0-zero-sprechi-luci.yaml) | Spegnimento automatico luci all'uscita |
| [docs/DIPENDENZE.md](docs/DIPENDENZE.md) | Entità e integrazioni richieste |
| [docs/REQUISITI_HARDWARE.md](docs/REQUISITI_HARDWARE.md) | Hardware necessario e compatibilità |
| [docs/GUIDA_HELPER_UI.md](docs/GUIDA_HELPER_UI.md) | Creazione o verifica helper dalla UI |
| [docs/GUIDA_PERSONALIZZAZIONE.md](docs/GUIDA_PERSONALIZZAZIONE.md) | Entity ID e impostazioni personalizzabili |
| [docs/GUIDA_CARD_TEST.md](docs/GUIDA_CARD_TEST.md) | Installazione e utilizzo card test Lovelace |
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

