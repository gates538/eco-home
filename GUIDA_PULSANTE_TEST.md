# Guida pulsante test Eco home v1.1

Il pulsante di test serve per provare voce, volume, Nest Hub, TTS e muting TV senza dover uscire e rientrare in casa.

L'automazione usa questo helper:

```yaml
input_button.echo_home_test_vocale
```

## Metodo consigliato: package YAML

Se usi il file:

```text
packages/eco-home-helpers-v1.1.yaml
```

il pulsante e' gia' incluso:

```yaml
input_button:
  echo_home_test_vocale:
    name: Eco home test vocale
    icon: mdi:speaker-message
```

Per usarlo:

1. Copia `packages/eco-home-helpers-v1.1.yaml` in `/config/packages/`.
2. Controlla che `configuration.yaml` contenga:

```yaml
homeassistant:
  packages: !include_dir_named packages
```

3. Riavvia Home Assistant oppure ricarica gli helper, se disponibile.
4. Cerca l'entita':

```text
input_button.echo_home_test_vocale
```

## Metodo da interfaccia Home Assistant

Se preferisci crearlo dalla UI:

1. Vai in **Impostazioni**.
2. Apri **Dispositivi e servizi**.
3. Vai su **Aiutanti**.
4. Clicca **Crea aiutante**.
5. Scegli **Pulsante**.
6. Nome:

```text
Eco home test vocale
```

7. Salva.

Poi controlla l'ID entita'. Deve essere:

```text
input_button.echo_home_test_vocale
```

Se Home Assistant crea un ID diverso, apri le impostazioni dell'entita' e rinominalo.

## Come aggiungerlo alla dashboard

1. Apri la dashboard dove vuoi il pulsante.
2. Clicca i tre puntini in alto a destra.
3. Scegli **Modifica dashboard**.
4. Aggiungi una card **Pulsante**.
5. Entita':

```text
input_button.echo_home_test_vocale
```

6. Nome consigliato:

```text
Test Eco home
```

7. Icona consigliata:

```text
mdi:speaker-message
```

## Cosa deve succedere quando lo premi

Il Nest Hub deve dire una frase simile:

```text
Echo Home e' attivo. Test vocale completato.
```

Se Eco home e' disattivato tramite `input_boolean.echo_home_attivo`, dira' che i messaggi automatici sono spenti.

## Se non funziona

Controlla questi punti:

- l'entita' deve chiamarsi esattamente `input_button.echo_home_test_vocale`;
- il TTS deve essere corretto in `tts_engine`;
- lo speaker deve essere corretto in `speaker`;
- se `debug: true`, guarda il Logbook di Home Assistant;
- verifica che l'automazione `Eco home` sia attiva.

