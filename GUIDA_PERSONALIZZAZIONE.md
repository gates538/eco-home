# Guida alla personalizzazione di Eco Home v1.1.2

Questa guida indica le sezioni principali da adattare senza fare affidamento su numeri di riga, che possono cambiare tra le versioni.

## Persone tracciate

Cerca `person.stefano` e `person.laura` nei trigger, in `tracked_people` e nelle variabili `arrived_stefano`, `arrived_laura` e `arrived_now_couple`.

Gli stessi entity ID devono essere usati in tutte queste sezioni. La versione 1.1.2 usa gli entity ID per scegliere i nomignoli e non dipende dal `friendly_name` completo.

## Nomignoli

Cerca:

```yaml
stefano_nicknames:
laura_nicknames:
couple_nicknames:
```

Puoi aggiungere, eliminare o sostituire le voci. Mantieni almeno un elemento in ogni lista.

## Sensore del portone

Cerca:

```yaml
door_sensor: binary_sensor.porta_contact
```

e il trigger `door_opened`. La configurazione predefinita usa `on` per indicare l'apertura. Se il tuo sensore usa `off`, aggiorna sia il trigger sia `trigger_door_open_valid`.

## Finestra temporale

```yaml
arrival_person_door_window_seconds: 300
arrival_group_window_seconds: 3
welcome_cooldown_seconds: 20
```

- `300`: massimo 5 minuti tra presenza e portone, in entrambi gli ordini.
- `3`: attesa prima del messaggio per raggruppare arrivi ravvicinati.
- `20`: protezione tra annunci consecutivi.

## Nest Hub e TTS

Aggiorna `speaker`, `tts_engine` e gli entity ID presenti nelle azioni `media_player.volume_set`, `media_player.media_stop` e `tts.speak`.

## TV

Aggiorna `tv_media_player` e gli entity ID delle azioni `media_player.volume_mute`.

Per disattivare la funzione:

```yaml
tv_ducking_enabled: false
```

## Luce

Aggiorna `light_entity` e l'entity ID dell'azione `light.turn_on`.

Parametri principali:

```yaml
light_brightness_pct: 45
light_kelvin: 4000
```

## Asciugatrice

Aggiorna:

```yaml
dryer_state_sensor:
dryer_completion_sensor:
```

La durata del promemoria è controllata da:

```yaml
dryer_announce_valid_hours: 12
```

## Debug

Durante le prove lascia:

```yaml
debug: true
```

Quando il comportamento è stato verificato puoi impostare `false` per ridurre le registrazioni nel Logbook.


