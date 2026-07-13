# Diagnostica Eco Home v1.1.3

La card mostra informazioni persistenti anche quando `debug: false`.

## Campi

| Helper | Significato |
|---|---|
| `input_text.echo_home_ultimo_evento` | Ultimo trigger ricevuto |
| `input_text.echo_home_ultimo_esito` | Motivo dell'annuncio o del blocco |
| `input_text.echo_home_ultima_persona` | Ultima persona passata a `home` |
| `input_text.echo_home_ultimo_profilo` | Profilo vocale scelto |
| `input_text.echo_home_ultimo_messaggio` | Testo inviato al TTS, abbreviato a 250 caratteri |
| `input_datetime.echo_home_ultima_apertura_portone` | Ultima apertura valida del portone |
| `input_datetime.echo_home_ultimo_arrivo` | Ultimo passaggio valido di una persona a `home` |
| `input_datetime.echo_home_ultimo_annuncio` | Ultimo test o annuncio inviato al Nest Hub |

## Esiti comuni

- **In attesa della combinazione presenza e portone:** è arrivato soltanto uno dei due eventi.
- **Modalità silenziosa attiva:** la combinazione era possibile, ma il TTS è stato bloccato.
- **Annuncio bloccato dal cooldown:** un messaggio è stato riprodotto troppo recentemente.
- **Nest Hub non disponibile:** la combinazione è stata riconosciuta, ma il TTS non è stato tentato.
- **Stato iniziale non valido:** il trigger proveniva da `unknown` o `unavailable`.
- **Annuncio completato:** il messaggio è stato inviato e il volume è stato ripristinato.

## Logbook

Con `debug: true`, Eco Home aggiunge dettagli tecnici nel Logbook. Dopo aver verificato il funzionamento puoi impostare `debug: false`; la diagnostica nella card continuerà a essere aggiornata.

