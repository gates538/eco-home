# Guida al pulsante di test - Eco Home v1.1.2

Il pulsante verifica Nest Hub, TTS, volume e muting della TV senza dover simulare un rientro.

## Helper

L'automazione usa:

```text
input_button.echo_home_test_vocale
```

Puoi crearlo dalla UI:

1. apri **Impostazioni → Dispositivi e servizi → Aiutanti**;
2. seleziona **Crea aiutante → Pulsante**;
3. usa il nome `Eco home test vocale`;
4. verifica che l'entity ID sia `input_button.echo_home_test_vocale`.

## Utilizzo

Premi il pulsante dalla pagina degli helper oppure dalla card Lovelace inclusa nel repository.

Il Nest Hub deve pronunciare un messaggio di conferma. Il test controlla il percorso audio, ma non modifica gli stati delle persone o del portone.

Per provare la logica completa è necessario un vero passaggio `not_home → home` abbinato all'apertura del portone entro la finestra configurata.

## Se non funziona

Controlla:

- che l'helper esista con l'entity ID esatto;
- che l'automazione `Eco home` sia attiva;
- che `media_player.nest_hub_sala` sia disponibile;
- che `tts.google_ai_tts` funzioni;
- la traccia dell'ultima esecuzione.


