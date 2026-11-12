<div align="center">

# 🌿 Eco Home — v2.0.0

**Ecosistema domotico integrato, modulare e con intelligenza artificiale multimodale per Home Assistant.**

[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-2026.x-41BDF5?style=flat-square&logo=homeassistant&logoColor=white)](https://www.home-assistant.io/)
[![Release](https://img.shields.io/badge/versione-v2.0.0-2ea44f?style=flat-square)](CHANGELOG.md)
[![Formato](https://img.shields.io/badge/formato-YAML-CB171E?style=flat-square&logo=yaml&logoColor=white)](CHANGELOG.md)
[![GitHub Sponsors](https://img.shields.io/badge/GitHub%20Sponsors-Support-EA4AAA?style=flat-square&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/gates538)
[![PayPal](https://img.shields.io/badge/PayPal-Offrimi%20un%20caff%C3%A8-00457C?style=flat-square&logo=paypal&logoColor=white)](https://www.paypal.me/gates538)

</div>

---

## 🏛️ Architettura del Progetto

Il progetto raccoglie **102 automazioni** e **105 script** organizzati in un'architettura modulare, scalabile e completamente anonimizzata:

```text
eco-home/
├── automations/      # 7 moduli logici di automazione (102 automazioni totali)
├── scripts/          # 6 moduli script operativi e AI per Home Assistant (105 script totali)
└── docs/             # Guide tecniche, dipendenze e requisiti hardware
```

---

## ⚡ Moduli di Automazione Attivi (`/automations`)

| Modulo | Descrizione Principale |
|---|---|
| [`01_sicurezza_e_presenza.yaml`](automations/01_sicurezza_e_presenza.yaml) | Centrale allarme, perimetrale notturno, dissuasione visiva, geofencing, accoglienza ospiti one-shot, modalità ospiti cameretta e presidio PTZ. |
| [`02_clima_e_riscaldamento.yaml`](automations/02_clima_e_riscaldamento.yaml) | Gestione Termocamino a pellet (con notifica interattiva pre-pranzo e posticipo), climatizzatori Samsung, pompa di calore ACS (boost ospiti) e raffreddamento apparati di rete. |
| [`03_animali_petcare.yaml`](automations/03_animali_petcare.yaml) | Fotoperiodo biologico anti-alghe acquario (FZONE BLE), alimentazione intelligente VSON Smart, ossigenatore e monitoraggio completo Petkit (dispenser e fontanella). |
| [`04_casa_ed_elettrodomestici.yaml`](automations/04_casa_ed_elettrodomestici.yaml) | Automazioni robot aspirapolvere Dreame (Clean Genius in assenza e rientro automatico), sicurezza piano induzione/forno/frigo/freezer, asciugatrice e anti-blackout 6 kW. |
| [`05_luci_cinema_comfort.yaml`](automations/05_luci_cinema_comfort.yaml) | Gestione luci 4000K, telecomandi Zigbee (Hue Tap Dial & telecomando divano con doppio click), scena Cinema, LED blu BTicino Living Now e fessure tapparelle. |
| [`06_meteo_e_automobili.yaml`](automations/06_meteo_e_automobili.yaml) | Stazione meteo Netatmo (pioggia, vento, allerta temporale con scenario interattivo), bollettini Protezione Civile (DPC) e aggiornamenti traffico pendolari. |
| [`07_sistema_e_notifiche.yaml`](automations/07_sistema_e_notifiche.yaml) | Watchdog Zigbee2MQTT/SLZB-06, NAS Synology, auto-healing telecamere Mesh, auto-update Docker & HACS, DDNS/SSL, IP ban interattivo, routine AI e pillole sarcastiche. |

---

## 📜 Moduli Script Attivi (`/scripts`)

| Modulo | Descrizione |
|---|---|
| [`01_tapparelle.yaml`](scripts/01_tapparelle.yaml) | Posizionamento tapparelle (totale, fessure aperte 8%, percentuale custom) e scenari globali (Entra, Esci, Estate, Inverno, Temporale, Preparazione Notte). |
| [`02_animali.yaml`](scripts/02_animali.yaml) | Gestione acquario (modalità ammirazione ospiti, buio 24h, pasto con fermo pompa), dosaggio Petkit, pulizia lettiera, programmi robot aspirapolvere e report vocale. |
| [`03_comfort_clima.yaml`](scripts/03_comfort_clima.yaml) | Gestione sospensione sveglie, scenari buonanotte, modalità ospiti cameretta, boost ACS pompa di calore, posticipo accensione camino e interrogazioni vocali di stato. |
| [`04_telecamere_tablet.yaml`](scripts/04_telecamere_tablet.yaml) | Controllo PTZ multi-preset, calibrazione Home, scansione autonoma parcheggio e analisi AI multimodale (Gemini Vision) su telecamere, fiamma camino e varchi. |
| [`05_notifiche_smart.yaml`](scripts/05_notifiche_smart.yaml) | Motore centralizzato `notifica_smart`, annunci vocali AI generativi (rientro, cucina, frigo, buongiorno, weekend, rifiuti, ospiti), pillole sarcastiche e lista spesa vocale. |
| [`06_manutenzione_ha.yaml`](scripts/06_manutenzione_ha.yaml) | Controllo centrale sicurezza, orchestrazione container Docker su NAS Synology, aggiornamento automatico integrazioni HACS e verifica stato tunnel VPN. |

---

## 📚 Documentazione (`/docs`)

- [**DIPENDENZE.md**](docs/DIPENDENZE.md): Entità, piattaforme e integrazioni richieste.
- [**REQUISITI_HARDWARE.md**](docs/REQUISITI_HARDWARE.md): Scheda tecnica dispositivi e coordinator Zigbee.
- [**GUIDA_HELPER_UI.md**](docs/GUIDA_HELPER_UI.md): Helper e interruttori virtuali configurati.
- [**GUIDA_PERSONALIZZAZIONE.md**](docs/GUIDA_PERSONALIZZAZIONE.md): Personalizzazione orari, soglie e nomi.
- [**GUIDA_CARD_TEST.md**](docs/GUIDA_CARD_TEST.md): Collaudo e pulsanti test per Lovelace.

---

