# Personalizzazione Eco Home v1.1.4

I numeri di riga si riferiscono a `eco-home-v1.1.4.yaml` pubblicato con la release.

## Persone

Alle righe **9-10** e **573-574** sostituisci:

```text
person.stefano
person.laura
```

Se cambi questi entity ID, sostituisci anche tutte le occorrenze nei blocchi `arrived_stefano`, `arrived_laura` e `arrived_now_couple`, circa alle righe **317-327**.

## Portone

L'entità compare alla riga **18** e nella variabile `door_sensor` alla riga **568**:

```text
binary_sensor.porta_contact
```

La configurazione considera il portone aperto quando passa a `on`.

## Nest Hub e TTS

Controlla tutte le occorrenze di:

```text
media_player.nest_hub_sala
tts.google_ai_tts
```

Le variabili principali sono alle righe **564-565**. Gli stessi entity ID vengono usati anche nelle azioni TTS e di ripristino volume.

## TV e luce

```text
media_player.tv_sala_ue85du7170uxzt
light.luceambiente
```

Le variabili sono alle righe **566-567**. Sostituisci anche le occorrenze nelle azioni della parte superiore del file.

## Asciugatrice

Controlla:

```text
sensor.esterno_asciugatrice_machine_state
sensor.esterno_asciugatrice_completion_time
sensor.esterno_asciugatrice_energia_elettrica
```

Le variabili si trovano circa alle righe **569-571**. Il sensore di energia è predisposto ma non è indispensabile per il promemoria.

## Tempi e volumi

| Impostazione | Riga | Valore predefinito |
|---|---:|---:|
| Assenza minima | 587 | 2 minuti |
| Finestra presenza-portone | 588 | 300 secondi |
| Attesa gruppo | 589 | 3 secondi |
| Cooldown annunci | 590 | 20 secondi |
| Volume giorno | 594 | 0.8 |
| Volume sera | 595 | 0.8 |
| Volume notte | 596 | 0.4 |
| Luminosità luce | 604 | 45% |

## Debug

Alla riga **562**:

```yaml
debug: true
```

Imposta `false` quando l'automazione è stabile e non vuoi più messaggi diagnostici nel Logbook. Gli helper della card continueranno ad aggiornarsi.

## Card

Gli entity ID delle persone e dei dispositivi sono presenti anche in `eco-home-v1.1.4-dashboard-card.yaml` e devono corrispondere a quelli dell'automazione.

