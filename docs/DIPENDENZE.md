# Dipendenze di Eco Home v1.5.0

Eco Home usa esclusivamente funzioni standard di Home Assistant. Non richiede HACS o componenti personalizzati.

Questo file elenca le dipendenze software e gli entity ID dell'ecosistema completo v1.5.0.

---

## Entità Principali

```text
person.stefano
person.laura
binary_sensor.porta_contact
media_player.nest_hub_sala
tts.google_translate_it_lt
```

Le persone devono passare correttamente a `home` e `not_home`. Il portone deve passare a `on` quando viene aperto.

La sintesi vocale utilizza `tts.google_translate_it_lt` (con lingua `it` e tld `it`) sul Nest Hub Sala.

---

## Entità Opzionali e Sensori di Casa

```text
light.luceambiente
light.faretti_cucina
media_player.sala_tv_sala
media_player.emby_homeassistant
sensor.temperatura_media
sensor.temperatura_media_esterna
sensor.sala_anemometro_gust_strength
sensor.terrazza_pulvirometro_precipitazione
sensor.cucina_piano_cottura_stato_di_funzionamento
sensor.cucina_piano_cottura_potenza
sensor.cucina_forno_machine_state
sensor.esterno_asciugatrice_machine_state
vacuum.dreame_l40_pro (o vacuum.dobby)
image.dispenser_crocchette_ultimo_pasto
climate.condizionatore_sala
climate.condizionatore_camera
camera.sala_2
sun.sun
```

---

## Helper Configurazione UI

```text
input_boolean.eco_home_attivo
input_boolean.eco_home_silenzioso
input_boolean.eco_home_modalita_ferie
input_boolean.eco_home_allarme_inserito
input_boolean.eco_home_notifiche_foto
input_boolean.eco_home_asciugatrice_da_annunciare
input_datetime.eco_home_asciugatrice_fine
input_datetime.eco_home_ultimo_annuncio
input_datetime.eco_home_ultima_apertura_portone
input_datetime.eco_home_ultimo_arrivo
input_button.eco_home_test_vocale
input_select.eco_home_scenario_test
input_text.eco_home_ultimo_evento
input_text.eco_home_ultimo_esito
input_text.eco_home_ultimo_profilo
input_text.eco_home_ultimo_messaggio
input_text.eco_home_ultima_persona
```

---

## Controllo prima dell'uso

1. Verifica gli entity ID in **Strumenti per sviluppatori → Stati**.
2. Controlla che il portone sia `off` quando chiuso e `on` quando aperto.
3. Esegui **Ricarica automazioni e script** in Home Assistant.
