# Dipendenze di Eco Home

Eco Home è un'automazione YAML per Home Assistant e non richiede librerie Python, pacchetti Node.js o un file `requirements.txt`.

Le dipendenze del progetto sono integrazioni, entità e helper di Home Assistant. Prima di importare `eco-home-v1.1.1.yaml`, verifica quanto segue.

## Dipendenze obbligatorie

### Home Assistant

È necessaria un'installazione di Home Assistant in grado di gestire automazioni YAML e le azioni usate dal progetto.

### Persone tracciate

L'automazione è configurata per queste entità:

```text
person.stefano
person.laura
```

Devono passare correttamente tra `home` e `not_home`. Se i tuoi entity ID sono diversi, sostituiscili nell'automazione.

### Sensore del portone

Entità configurata:

```text
binary_sensor.porta_contact
```

L'automazione considera il portone aperto quando il sensore passa a `on`.

Se il tuo sensore usa `off` per indicare l'apertura, modifica il relativo trigger.

### Altoparlante o Nest Hub

Entità configurata:

```text
media_player.nest_hub_sala
```

Il dispositivo deve supportare almeno:

```text
media_player.volume_set
media_player.media_stop
```

### Motore TTS

Entità configurata:

```text
tts.google_ai_tts
```

L'automazione usa l'azione:

```text
tts.speak
```

Il motore TTS deve essere già configurato e funzionante in Home Assistant.

### Integrazione Sun

L'accensione della luce quando fuori è buio usa:

```text
sun.sun
```

Questa entità è normalmente disponibile quando è attiva la configurazione predefinita di Home Assistant.

## Helper richiesti

Eco Home utilizza questi helper:

```text
input_boolean.echo_home_attivo
input_boolean.echo_home_silenzioso
input_boolean.echo_home_asciugatrice_da_annunciare
input_datetime.echo_home_asciugatrice_fine
input_datetime.echo_home_ultimo_annuncio
input_button.echo_home_test_vocale
```

Puoi crearli dalla UI di Home Assistant oppure usare il seguente package YAML:

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

Per usare il blocco come package, salvalo per esempio in:

```text
/config/packages/eco-home-helpers-v1.1.yaml
```

Poi verifica che `configuration.yaml` contenga:

```yaml
homeassistant:
  packages: !include_dir_named packages
```

## Dipendenze legate alle funzioni opzionali

### Luce ambiente

Entità configurata:

```text
light.luceambiente
```

Viene accesa al rientro soltanto quando `sun.sun` è sotto l'orizzonte. Se non vuoi questa funzione, rimuovi o disabilita il relativo blocco `light.turn_on`.

### TV con muting temporaneo

Entità configurata:

```text
media_player.tv_sala_ue85du7170uxzt
```

Per il muting temporaneo deve supportare:

```text
media_player.volume_mute
```

La funzione può essere disattivata impostando:

```yaml
tv_ducking_enabled: false
```

### Asciugatrice

Entità configurate:

```text
sensor.esterno_asciugatrice_machine_state
sensor.esterno_asciugatrice_completion_time
```

La prima segnala lo stato del ciclo; la seconda deve fornire una data e ora interpretabile da Home Assistant per calcolare i minuti rimanenti.

Questa entità è dichiarata tra le variabili, ma nella versione `v1.1.1` non viene utilizzata dalla logica:

```text
sensor.esterno_asciugatrice_energia_elettrica
```

Non è quindi una dipendenza effettiva della versione corrente.

## Azioni Home Assistant utilizzate

L'automazione richiama queste azioni:

```text
tts.speak
media_player.volume_set
media_player.volume_mute
media_player.media_stop
light.turn_on
input_boolean.turn_on
input_boolean.turn_off
input_datetime.set_datetime
logbook.log
```

## Componenti non richiesti

Eco Home non richiede:

- HACS;
- componenti personalizzati;
- API esterne per generare le frasi;
- librerie Python aggiuntive;
- `requirements.txt`;
- `package.json`.

## Controllo prima dell'installazione

1. Verifica tutti gli entity ID in **Strumenti per sviluppatori → Stati**.
2. Prova il motore TTS sul Nest Hub.
3. Crea gli helper richiesti.
4. Controlla lo stato usato dal sensore del portone quando viene aperto.
5. Importa l'automazione.
6. Esegui **Controlla configurazione**.
7. Ricarica le automazioni e usa il pulsante di test vocale.
