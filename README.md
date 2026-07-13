# Eco home

Automazione Home Assistant per un messaggio di benvenuto sul Nest Hub quando il rientro e' confermato da una combo:

- una persona tracciata passa a `home`;
- entro 5 minuti si apre il portone;
- dopo 3 secondi parte il messaggio.

Include anche:

- luce ambiente accesa subito solo se fuori e' buio;
- volume TTS 80% di giorno/sera e 40% di notte;
- muting temporaneo della TV durante il messaggio;
- promemoria asciugatrice se finisce mentre non c'e' nessuno in casa;
- frasi locali random senza chiamate AI esterne.

## Supporto

Se Eco home ti e' utile e vuoi offrirmi un caffe':

[![Offrimi un caffe'](https://img.shields.io/badge/Offrimi%20un%20caffe'-☕-yellow)](https://github.com/sponsors/gates538)

## File

- `eco-home-v1.1.yaml`: automazione completa da copiare in `automations.yaml` o importare/modificare dalla UI di Home Assistant.
- `GUIDA_PERSONALIZZAZIONE.md`: elenco delle voci da modificare con linee e spiegazioni.
- `GUIDA_PULSANTE_TEST.md`: guida per creare e usare il pulsante di test vocale.
- `packages/eco-home-helpers-v1.1.yaml`: helper necessari, utile se non li hai gia' creati.

Alias visibile in Home Assistant:

```text
Eco home
```
## Entita' da adattare

Controlla questi entity id prima di usarla:

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

1. Copia `eco-home-v1.1.yaml` dentro `automations.yaml` oppure importa l'automazione dalla UI.
2. Se non hai gia' gli helper, copia `packages/eco-home-helpers-v1.1.yaml` in `/config/packages/`.
3. Se usi i package, assicurati che `configuration.yaml` contenga:

```yaml
homeassistant:
  packages: !include_dir_named packages
```

4. Controlla le entita' indicate in `GUIDA_PERSONALIZZAZIONE.md`.
5. Se vuoi testare manualmente la voce, segui `GUIDA_PULSANTE_TEST.md`.
6. Da Home Assistant esegui Controlla configurazione e poi Ricarica automazioni.

## Logica principale

La voce non parte quando la persona viene rilevata a casa. Quel trigger serve solo come memoria del rientro.

La voce parte solo quando si apre il portone e almeno una persona tracciata e' stata rilevata `home` negli ultimi 5 minuti.

## Note

Se il sensore porta usa `off` per indicare aperto, cambia il trigger del portone da:

```yaml
to: 'on'
```

a:

```yaml
to: 'off'
```
