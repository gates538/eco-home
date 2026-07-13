# Dipendenze di Eco Home v1.1.4

Eco Home usa esclusivamente funzioni standard di Home Assistant. Non richiede HACS o componenti personalizzati.

## Entità obbligatorie

Adatta questi entity ID alla tua installazione:

```text
person.stefano
person.laura
binary_sensor.porta_contact
media_player.nest_hub_sala
tts.google_ai_tts
```

Le persone devono passare correttamente a `home`. Il portone deve passare a `on` quando viene aperto.

## Entità opzionali

```text
light.luceambiente
media_player.tv_sala_ue85du7170uxzt
sensor.esterno_asciugatrice_machine_state
sensor.esterno_asciugatrice_completion_time
sensor.esterno_asciugatrice_energia_elettrica
```

Se non utilizzi una funzione opzionale, disattiva o rimuovi i relativi blocchi seguendo [GUIDA_PERSONALIZZAZIONE.md](GUIDA_PERSONALIZZAZIONE.md).

## Helper

Per una nuova installazione copia
`eco-home-v1.1.4-helpers.yaml` in `/config/packages/eco-home-v1.1.4-helpers.yaml`.

Se preferisci crearli dalla UI, segui [GUIDA_HELPER_UI.md](GUIDA_HELPER_UI.md).

Se aggiorni dalla 1.1.3 o da una versione precedente, non caricare il nuovo
package insieme al vecchio. Segui prima [GUIDA_AGGIORNAMENTO.md](GUIDA_AGGIORNAMENTO.md)
per migrare da `echo_home_*` a `eco_home_*`.

Il file completo definisce:

```text
input_boolean.eco_home_attivo
input_boolean.eco_home_silenzioso
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

Per abilitare i package, `configuration.yaml` contiene:

```yaml
homeassistant:
  packages: !include_dir_named packages
```

Non mantenere contemporaneamente helper `echo_home_*` e `eco_home_*`: la
versione corrente utilizza esclusivamente il prefisso `eco_home_*`.

## Controllo prima dell'uso

1. Verifica gli entity ID in **Strumenti per sviluppatori → Stati**.
2. Controlla che il portone sia `on` quando aperto.
3. Prova `tts.google_ai_tts` sul Nest Hub.
4. Esegui **Controlla configurazione**.
5. Ricarica package e automazioni oppure riavvia Home Assistant.
6. Seleziona `Percorso audio` dalla card ed esegui il test.

