# Personalizzazione Eco Home v1.1.6

I numeri di riga si riferiscono a `eco-home-v1.1.6.yaml` pubblicato con la release.

## Persone

Alle righe **10-11** e **661-662** sostituisci:

```text
person.stefano
person.laura
```

Se cambi questi entity ID, sostituisci anche tutte le occorrenze nei blocchi `arrived_stefano`, `arrived_laura` e `arrived_now_couple`, circa alle righe **317-329**.

## Portone

L'entità compare alla riga **19** e nella variabile `door_sensor` alla riga **651**:

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

Le variabili principali sono alle righe **647-648**. Gli stessi entity ID vengono usati anche nelle azioni TTS e di ripristino volume.

Non scegliere il lettore soltanto perché compare come `media_player`: deve
superare le prove TTS, volume e arresto descritte in
[REQUISITI_HARDWARE.md](REQUISITI_HARDWARE.md#4-altoparlante-o-display-per-il-tts).

## TV e luce

```text
media_player.tv_sala_ue85du7170uxzt
light.luceambiente
```

Le variabili sono alle righe **649-650**. Sostituisci anche le occorrenze nelle azioni della parte superiore del file.

## Asciugatrice

Controlla:

```text
sensor.esterno_asciugatrice_machine_state
sensor.esterno_asciugatrice_completion_time
sensor.esterno_asciugatrice_energia_elettrica
```

Le variabili si trovano circa alle righe **652-654**. Il sensore di energia è predisposto ma non è indispensabile per il promemoria.

## Tempi e volumi

| Impostazione | Riga | Valore predefinito |
|---|---:|---:|
| Assenza minima | 676 | 2 minuti |
| Finestra presenza-portone | 677 | 300 secondi |
| Attesa gruppo | 678 | 0 secondi |
| Cooldown annunci | 679 | 20 secondi |
| Volume giorno | 683 | 0.8 |
| Volume sera | 684 | 0.8 |
| Volume notte | 685 | 0.4 |
| Luminosità luce | 693 | 45% |

## Debug

Alla riga **645**:

```yaml
debug: true
```

Imposta `false` quando l'automazione è stabile e non vuoi più messaggi diagnostici nel Logbook. Gli helper della card continueranno ad aggiornarsi.

## Telecamera e Notifiche Foto

Le nuove variabili configurabili per la telecamera e le notifiche si trovano nella sezione `variables:` dell'automazione:

- `camera_entity`: L'entity ID della telecamera (default: `camera.sala_2`).
- `stefano_notification_service`: Il servizio di notifica per Stefano (default: `notify.notify` per tutti i dispositivi. Cambialo es. in `notify.mobile_app_stefano` per inviarlo solo a Stefano).
- `laura_notification_service`: Il servizio di notifica per Laura (default: `notify.notify`).
- `snapshot_file_path`: Il percorso su disco dove salvare temporaneamente lo snapshot (default: `/config/www/snapshots/eco_home_sala_2.jpg`).
- `snapshot_access_url`: L'URL locale per l'allegato notifica (default: `/local/snapshots/eco_home_sala_2.jpg`).

La notifica verrà inviata **solo se la casa era completamente vuota** prima del rientro rilevato.

## Card

Gli entity ID delle persone e dei dispositivi sono presenti anche in `eco-home-v1.1.6-dashboard-card.yaml` e devono corrispondere a quelli dell'automazione.

