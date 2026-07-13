# Eco home v1.1.1

> Versione archiviata. Per le nuove installazioni usa la versione corrente nella cartella principale del repository.

Automazione Home Assistant per un messaggio di benvenuto sul Nest Hub quando il rientro e' confermato dalla combinazione tra presenza e portone.

La conferma funziona in entrambi gli ordini:

- una persona tracciata passa a `home` e, entro 5 minuti, si apre il portone;
- si apre il portone e, entro 5 minuti, una persona tracciata passa a `home`;
- dopo la conferma, il messaggio parte con un breve ritardo di 3 secondi.

Questo rende il rientro piu' affidabile quando GPS o Wi-Fi aggiornano la presenza dopo l'apertura del portone.

Include anche:

- luce ambiente accesa subito solo se fuori e' buio;
- volume TTS 80% di giorno/sera e 40% di notte;
- muting temporaneo della TV durante il messaggio;
- promemoria asciugatrice se finisce mentre non c'e' nessuno in casa;
- frasi locali casuali senza chiamate AI esterne.

## Supporto

Se Eco home ti e' utile e vuoi offrirmi un caffe':

[![Offrimi un caffe'](https://img.shields.io/badge/Offrimi%20un%20caffe'-☕-yellow)](https://github.com/sponsors/gates538)

## File

- `eco-home-v1.1.1.yaml`: automazione completa da copiare in `automations.yaml` o importare/modificare dalla UI di Home Assistant.
- [`CHANGELOG.md`](../../CHANGELOG.md): cronologia delle modifiche tra le versioni.
- [`GUIDA_PERSONALIZZAZIONE.md`](../../GUIDA_PERSONALIZZAZIONE.md): elenco delle voci da modificare con linee e spiegazioni.
- [`GUIDA_PULSANTE_TEST.md`](../../GUIDA_PULSANTE_TEST.md): guida per creare e usare il pulsante di test vocale.
- `eco-home-v1.1.1-dashboard-card.yaml`: card Lovelace per controllare e testare Eco Home dalla plancia.
- [`GUIDA_CARD_TEST.md`](../../GUIDA_CARD_TEST.md): guida per installare e utilizzare la card di test.

Alias visibile in Home Assistant:

```text
Eco home
```

Versione:

```text
v1.1.1
```

## Entita' da adattare

Controlla questi entity ID prima di usarla:

- `person.stefano`
- `person.laura`
- `binary_sensor.porta_contact`
- `media_player.nest_hub_sala`
- `tts.google_ai_tts`
- `media_player.tv_sala_ue85du7170uxzt`
- `light.luceambiente`
- `sensor.esterno_asciugatrice_machine_state`
- `sensor.esterno_asciugatrice_completion_time`
- `input_boolean.echo_home_attivo`
- `input_boolean.echo_home_silenzioso`
- `input_boolean.echo_home_asciugatrice_da_annunciare`
- `input_datetime.echo_home_asciugatrice_fine`
- `input_datetime.echo_home_ultimo_annuncio`
- `input_button.echo_home_test_vocale`

## Installazione rapida

1. Copia `eco-home-v1.1.1.yaml` dentro `automations.yaml` oppure importa l'automazione dalla UI.
2. Controlla le entita' indicate nella [`GUIDA_PERSONALIZZAZIONE.md`](../../GUIDA_PERSONALIZZAZIONE.md).
3. Se vuoi testare manualmente la voce, segui la [`GUIDA_PULSANTE_TEST.md`](../../GUIDA_PULSANTE_TEST.md).
4. Da Home Assistant esegui **Controlla configurazione** e poi **Ricarica automazioni**.

## Logica principale

Il rientro viene confermato quando presenza e portone si verificano entro una finestra di 5 minuti, indipendentemente dall'ordine degli eventi.

L'apertura recente rimane valida anche se il portone viene richiuso prima dell'aggiornamento della posizione del telefono.

## Note

Se il sensore porta usa `off` per indicare aperto, cambia il trigger del portone da:

```yaml
to: 'on'
```

a:

```yaml
to: 'off'
```

