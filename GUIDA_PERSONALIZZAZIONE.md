# Guida personalizzazione Eco home v1.1

Questa guida indica le parti principali da modificare in `eco-home-v1.1.yaml`.

Le linee possono cambiare se modifichi il file, ma sono corrette per questa versione.

## Persone tracciate

Linee 9-11:

```yaml
entity_id:
- person.stefano
- person.laura
```

Sostituisci con le tue persone Home Assistant.

Linee 337-339:

```yaml
tracked_people:
- person.stefano
- person.laura
```

Devono essere uguali alle persone usate nei trigger.

## Sensore portone

Linee 14-17:

```yaml
entity_id: binary_sensor.porta_contact
to: 'on'
```

Modifica `binary_sensor.porta_contact` con il tuo sensore.

Se il tuo sensore usa `off` per porta aperta, cambia:

```yaml
to: 'on'
```

in:

```yaml
to: 'off'
```

Aggiorna anche la variabile alla linea 333:

```yaml
door_sensor: binary_sensor.porta_contact
```

## Nest Hub e TTS

Linee 329-330:

```yaml
speaker: media_player.nest_hub_sala
tts_engine: tts.google_ai_tts
```

Modifica con il tuo speaker e il tuo motore TTS.

Nel file ci sono anche riferimenti diretti nelle azioni:

- linea 87: volume Nest Hub
- linee 93-95: TTS test
- linea 256: volume Nest Hub rientro
- linee 272-274: TTS rientro

Se cambi speaker o TTS, controlla anche queste linee.

## TV muta durante il messaggio

Linea 332:

```yaml
tv_media_player: media_player.tv_sala_ue85du7170uxzt
```

Modifica con la tua TV.

Linea 353:

```yaml
tv_ducking_enabled: true
```

Metti `false` se non vuoi mutare la TV.

Linee 80, 108, 249, 287:

```yaml
entity_id: media_player.tv_sala_ue85du7170uxzt
```

Se cambi TV, aggiorna anche questi riferimenti diretti.

## Luce ingresso/sala

Linea 331:

```yaml
light_entity: light.luceambiente
```

Linee 220 e 225:

```yaml
entity_id: light.luceambiente
```

Modifica con la tua luce.

Linee 360-361:

```yaml
light_brightness_pct: 45
light_kelvin: 4000
```

Personalizza luminosita' e temperatura colore.

La luce si accende solo se fuori e' buio:

Linee 216-218:

```yaml
entity_id: sun.sun
state: below_horizon
```

## Tempi principali

Linea 344:

```yaml
arrival_person_door_window_seconds: 300
```

Tempo massimo tra rilevamento `home` e apertura portone. `300` secondi = 5 minuti.

Linea 345:

```yaml
arrival_group_window_seconds: 3
```

Attesa dopo apertura portone prima dell'annuncio.

Linea 346:

```yaml
welcome_cooldown_seconds: 20
```

Tempo minimo tra due annunci di benvenuto.

## Volume

Linee 350-352:

```yaml
base_volume_day: 0.8
base_volume_evening: 0.8
base_volume_night: 0.4
```

Valori da `0.0` a `1.0`.

Esempi:

- `0.5` = 50%
- `0.8` = 80%
- `1.0` = 100%

## Asciugatrice

Linee 334-336:

```yaml
dryer_state_sensor: sensor.esterno_asciugatrice_machine_state
dryer_power_sensor: sensor.esterno_asciugatrice_energia_elettrica
dryer_completion_sensor: sensor.esterno_asciugatrice_completion_time
```

Modifica con i tuoi sensori.

Linea 347:

```yaml
dryer_announce_valid_hours: 12
```

Per quante ore resta valido l'annuncio "asciugatrice finita".

## Helper richiesti

Linee 340-341:

```yaml
input_boolean.echo_home_attivo
input_boolean.echo_home_silenzioso
```

Linee 122-127, 171, 174, 177, 193-195, 295-307, 407-411:

```yaml
input_boolean.echo_home_asciugatrice_da_annunciare
input_datetime.echo_home_asciugatrice_fine
input_datetime.echo_home_ultimo_annuncio
```

Linea 51:

```yaml
input_button.echo_home_test_vocale
```

Per creare e usare il pulsante di test, vedi:

```text
GUIDA_PULSANTE_TEST.md
```

Se non li hai gia', puoi usare il file:

```text
packages/eco-home-helpers-v1.1.yaml
```

## Debug

Linea 327:

```yaml
debug: true
```

Durante i test lascia `true`. Quando tutto funziona, puoi mettere:

```yaml
debug: false
```
