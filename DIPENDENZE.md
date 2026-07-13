# Dipendenze di Eco Home v1.1.2

Eco Home è un'automazione YAML per Home Assistant. Non richiede HACS, componenti personalizzati, librerie Python, Node.js o servizi AI esterni per generare le frasi.

## Dipendenze obbligatorie

Adatta questi entity ID alla tua installazione:

```text
person.stefano
person.laura
binary_sensor.porta_contact
media_player.nest_hub_sala
tts.google_ai_tts
```

Le persone devono passare correttamente tra `home` e `not_home`. Il sensore del portone deve produrre un cambio di stato quando viene aperto.

La configurazione predefinita considera il portone aperto quando passa a:

```yaml
to: "on"
```

Se il tuo sensore usa `off`, modifica sia il trigger sia il controllo `trigger_to_state` dell'automazione.

## Helper richiesti

```text
input_boolean.echo_home_attivo
input_boolean.echo_home_silenzioso
input_boolean.echo_home_asciugatrice_da_annunciare
input_datetime.echo_home_asciugatrice_fine
input_datetime.echo_home_ultimo_annuncio
input_button.echo_home_test_vocale
```

Gli helper della versione 1.1.1 restano compatibili con la 1.1.2.

Esempio di package:

```yaml
input_boolean:
  echo_home_attivo:
    name: Eco home attivo
    icon: mdi:home-assistant
  echo_home_silenzioso:
    name: Eco home silenzioso
    icon: mdi:volume-off
  echo_home_asciugatrice_da_annunciare:
    name: Eco home asciugatrice da annunciare
    icon: mdi:tumble-dryer-alert

input_datetime:
  echo_home_asciugatrice_fine:
    name: Eco home asciugatrice fine
    has_date: true
    has_time: true
  echo_home_ultimo_annuncio:
    name: Eco home ultimo annuncio
    has_date: true
    has_time: true

input_button:
  echo_home_test_vocale:
    name: Eco home test vocale
    icon: mdi:speaker-message
```

Per caricare i package, `configuration.yaml` deve contenere:

```yaml
homeassistant:
  packages: !include_dir_named packages
```

## Funzioni opzionali

```text
light.luceambiente
media_player.tv_sala_ue85du7170uxzt
sensor.esterno_asciugatrice_machine_state
sensor.esterno_asciugatrice_completion_time
```

- La luce viene accesa solo quando `sun.sun` è `below_horizon`.
- La TV deve supportare `media_player.volume_mute`.
- Il sensore di fine asciugatrice deve fornire una data interpretabile da Home Assistant.
- Il muting TV può essere disabilitato impostando `tv_ducking_enabled: false`.

## Controllo prima dell'installazione

1. Verifica gli entity ID in **Strumenti per sviluppatori → Stati**.
2. Prova il motore TTS sul Nest Hub.
3. Crea gli helper richiesti.
4. Controlla lo stato del sensore del portone quando viene aperto.
5. Inserisci l'automazione in `automations.yaml`.
6. Esegui **Controlla configurazione**.
7. Ricarica le automazioni e prova il pulsante vocale.


