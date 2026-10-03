<div align="center">

# 🌿 Eco Home — Casa Mancini

**Ecosistema domotico integrato e intelligente per Home Assistant.**

[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-Automation-41BDF5?style=flat-square&logo=homeassistant&logoColor=white)](https://www.home-assistant.io/)
[![Stato](https://img.shields.io/badge/architettura-modulare-2ea44f?style=flat-square)](CHANGELOG.md)
[![Formato](https://img.shields.io/badge/formato-YAML-CB171E?style=flat-square&logo=yaml&logoColor=white)](CHANGELOG.md)

</div>

---

## 🏛️ Architettura del Progetto

Il progetto è organizzato secondo un'architettura modulare chiara, scalabile e priva di ridondanze:

```text
eco-home/
├── automations/      # Moduli logici di automazione (01 - 07)
├── scripts/          # Moduli script operativi per Home Assistant (01 - 06)
├── docs/             # Guide tecniche, dipendenze e requisiti hardware
└── archive/          # Release storiche archiviate e ordinate per versione
```

---

## ⚡ Moduli di Automazione Attivi (`/automations`)

| Modulo | Descrizione Principale |
|---|---|
| [`01_sicurezza_e_presenza.yaml`](automations/01_sicurezza_e_presenza.yaml) | Centrale allarme, perimetrale, geofencing, sospensione ospiti, guardiano uscite e memoria presenze. |
| [`02_clima_e_riscaldamento.yaml`](automations/02_clima_e_riscaldamento.yaml) | Termoregolazione, gestione termocamino a pellet, climatizzazione e risparmio energetico finestre. |
| [`03_animali_petcare.yaml`](automations/03_animali_petcare.yaml) | Cura animali domestici (fontanella, lettiera Petkit Puramax 2, dispenser crocchette e gattaiola). |
| [`04_casa_ed_elettrodomestici.yaml`](automations/04_casa_ed_elettrodomestici.yaml) | Notifiche sicurezza cucina, monitoraggio frigo/freezer aperti, forno e asciugatrice. |
| [`05_luci_cinema_comfort.yaml`](automations/05_luci_cinema_comfort.yaml) | Scenari luminosi, modalità cinema Emby TV, gestione serale e automazioni zero sprechi. |
| [`06_meteo_e_automobili.yaml`](automations/06_meteo_e_automobili.yaml) | Previsioni meteo, monitoraggio pioggia, vento su terrazza e stato veicoli. |
| [`07_sistema_e_notifiche.yaml`](automations/07_sistema_e_notifiche.yaml) | Routine vocali buongiorno/buonanotte, notifiche smart smartphone/WhatsApp e manutenzione core. |

---

## 📜 Moduli Script Attivi (`/scripts`)

| Modulo | Descrizione |
|---|---|
| [`01_tapparelle.yaml`](scripts/01_tapparelle.yaml) | Posizionamento automatico e scenari tapparelle. |
| [`02_animali.yaml`](scripts/02_animali.yaml) | Routine igiene lettiera e dosaggio cibo. |
| [`03_comfort_clima.yaml`](scripts/03_comfort_clima.yaml) | Profili termici rapidi e booster riscaldamento. |
| [`04_telecamere_tablet.yaml`](scripts/04_telecamere_tablet.yaml) | Streaming live telecamere e gestione display. |
| [`05_notifiche_smart.yaml`](scripts/05_notifiche_smart.yaml) | Canali di dispatch prioritari (App S25/S22 & WhatsApp). |
| [`06_manutenzione_ha.yaml`](scripts/06_manutenzione_ha.yaml) | Backup programmato e polling diagnostico. |

---

## 📚 Documentazione (`/docs`)

- [**DIPENDENZE.md**](docs/DIPENDENZE.md): Entità, piattaforme e integrazioni richieste.
- [**REQUISITI_HARDWARE.md**](docs/REQUISITI_HARDWARE.md): Scheda tecnica dispositivi e coordinator Zigbee.
- [**GUIDA_HELPER_UI.md**](docs/GUIDA_HELPER_UI.md): Helper e interruttori virtuali configurati.
- [**GUIDA_PERSONALIZZAZIONE.md**](docs/GUIDA_PERSONALIZZAZIONE.md): Personalizzazione orari, soglie e nomi.
- [**GUIDA_CARD_TEST.md**](docs/GUIDA_CARD_TEST.md): Collaudo e pulsanti test per Lovelace.

---

## 📦 Archivio Versioni Storiche (`/archive`)

Le versioni monolitiche precedenti sono archiviate e ordinate nelle rispettive cartelle:
- [`archive/v1.1.1`](archive/v1.1.1) fino a [`archive/v1.1.8`](archive/v1.1.8)
- [`archive/v1.2.0`](archive/v1.2.0)
- [`archive/v1.3.0`](archive/v1.3.0)
- [`archive/v1.4.0`](archive/v1.4.0)
- [`archive/v1.5.0`](archive/v1.5.0)
