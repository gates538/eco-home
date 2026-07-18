# Personalizzazione Eco Home v1.1.8

I numeri di riga si riferiscono a `eco-home-v1.1.8.yaml` pubblicato con la release.

## Persone

Alle righe **10-11** e **795-796** sostituisci:

```text
person.stefano
person.laura
```

Se cambi questi entity ID, sostituisci anche tutte le occorrenze nei blocchi `arrived_stefano`, `arrived_laura` e `arrived_now_couple`, circa alle righe **340-360**.

## Portone

L'entità compare alla riga **19** e nella variabile `door_sensor` alla riga **779**:

```text
binary_sensor.porta_contact
```

La configurazione considera il portone aperto quando passa a `on`.
Prima di usarlo, verifica installazione e stati seguendo
[REQUISITI_HARDWARE.md](REQUISITI_HARDWARE.md#2-sensore-di-apertura-del-portone).

## Nest Hub e TTS

Controlla tutte le occorrenze di:

```text
media_player.nest_hub_sala
tts.google_ai_tts
```

Le variabili principali sono alle righe **775-776**. Gli stessi entity ID vengono usati anche nelle azioni TTS e di ripristino volume.

Non scegliere il lettore soltanto perché compare come `media_player`: deve
superare le prove TTS, volume e arresto descritte in
[REQUISITI_HARDWARE.md](REQUISITI_HARDWARE.md#4-altoparlante-o-display-per-il-tts).

## TV e luce

```text
media_player.tv_sala_ue85du7170uxzt
light.luceambiente
```

Le variabili sono alle righe **777-778**. Sostituisci anche le occorrenze nelle azioni della parte superiore del file.

## Asciugatrice

Controlla:

```text
sensor.esterno_asciugatrice_machine_state
sensor.esterno_asciugatrice_completion_time
sensor.esterno_asciugatrice_energia_elettrica
```

Le variabili si trovano circa alle righe **780-782**. Il sensore di energia è predisposto ma non è indispensabile per il promemoria.

## Tempi e volumi

| Impostazione | Riga | Valore predefinito |
|---|---:|---:|
| Assenza minima | 810 | 2 minuti |
| Finestra presenza-portone | 811 | 300 secondi |
| Attesa gruppo | 812 | 0 secondi |
| Cooldown annunci | 813 | 20 secondi |
| Volume giorno | 817 | 0.8 |
| Volume sera | 818 | 0.8 |
| Volume notte | 819 | 0.4 |
| Luminosità luce | 827 | 45% |

## Debug

Alla riga **773**:

```yaml
debug: true
```

Imposta `false` quando l'automazione è stabile e non vuoi più messaggi diagnostici nel Logbook. Gli helper della card continueranno ad aggiornarsi.

## Telecamera e Notifiche Foto

Le nuove variabili configurabili per la telecamera e le notifiche si trovano nella sezione `variables:` dell'automazione:

- `camera_entity`: L'entity ID della telecamera (default: `camera.sala_2`).
- `stefano_notification_service`: Il servizio di notifica per Stefano (default: `notify.notify` per tutti i dispositivi. Cambialo es. in `notify.mobile_app_stefano` per inviarlo solo a Stefano).
- `laura_notification_service`: Il servizio di notifica per Laura (default: `notify.notify`).
- `snapshot_file_path`: Il percorso su disco dove salvare temporaneamente lo snapshot (default: `/media/eco_home/eco_home_sala_2.jpg`).
- `snapshot_access_url`: L'URL locale per l'allegato notifica (default: `/media/local/eco_home/eco_home_sala_2.jpg`).

La notifica verrà inviata **solo se la casa era completamente vuota** prima del rientro rilevato.

## Temperatura e Condizionatori (Clima)

Le variabili per gestire il controllo del clima e della temperatura si trovano nella sezione `variables:` dell'automazione alle righe **788-793**:

- `indoor_temp_sensors`: La lista dei sensori di temperatura interna da monitorare (default: `sensor.temperatura_sala` e `sensor.temperatura_camera`). L'automazione ne calcolerà la media automatica.
- `ac_climate_entities`: La lista dei condizionatori (entità `climate.*`) da accendere in modalità raffrescamento al clic sulla notifica (default: `climate.condizionatore_sala` e `climate.condizionatore_camera`).

## Card

Gli entity ID delle persone e dei dispositivi sono presenti anche in `eco-home-v1.1.8-dashboard-card.yaml` e devono corrispondere a quelli dell'automazione.


