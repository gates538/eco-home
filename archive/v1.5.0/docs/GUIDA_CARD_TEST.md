# Guida alla card Eco Home v1.5.0

La card usa soltanto componenti standard di Home Assistant per controllare e monitorare l'intero ecosistema da dashboard.

## Requisiti

Prima di installarla verifica che siano presenti:
- l'automazione `Eco home` v1.5.0;
- gli helper indicati in [DIPENDENZE.md](DIPENDENZE.md);
- il nuovo helper `input_boolean.eco_home_modalita_ferie`.

## Codice Card Lovelace Completo

Copia e incolla questo blocco in una scheda **Manuale**:

```yaml
type: vertical-stack
cards:
  - type: entities
    title: 🏠 Eco Home v1.5.0 - Controlli
    show_header_toggle: false
    entities:
      - entity: input_boolean.eco_home_attivo
        name: Sistema Eco Home
      - entity: input_boolean.eco_home_silenzioso
        name: Modalità Silenziosa
      - entity: input_boolean.eco_home_modalita_ferie
        name: Modalità Ferie / Vacanze (Disattiva avvisi mattutini)
      - entity: input_boolean.eco_home_notifiche_foto
        name: Notifiche Foto al Rientro

  - type: entities
    title: 🧪 Scenario di Test Vocale
    show_header_toggle: false
    entities:
      - entity: input_select.eco_home_scenario_test
        name: Seleziona Scenario
      - entity: input_button.eco_home_test_vocale
        name: Avvia Prova Vocale Nest Hub

  - type: entities
    title: 📊 Diagnostica & Ultimo Evento
    show_header_toggle: false
    entities:
      - entity: input_text.eco_home_ultimo_profilo
        name: Ultimo Profilo
      - entity: input_text.eco_home_ultimo_evento
        name: Ultimo Evento
      - entity: input_text.eco_home_ultimo_messaggio
        name: Ultimo Messaggio
      - entity: input_datetime.eco_home_ultimo_annuncio
        name: Orario Ultimo Annuncio
```

## Sezioni della card

### Controlli
Permette di attivare/disattivare Eco Home, impostare la modalità silenziosa, attivare la **Modalità Ferie** (per non essere svegliati dagli avvisi meteo mattutini delle 07:40) e gestire le notifiche fotografiche.

### Scenario di test
Seleziona il profilo vocale ed esegue un test istantaneo sul Google Nest Hub.

### Diagnostica
Mostra in tempo reale l'ultimo profilo rilevato, l'evento, il messaggio pronunciato e l'orario esatto.


