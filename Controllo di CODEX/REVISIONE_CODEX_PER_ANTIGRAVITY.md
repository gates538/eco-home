# Revisione CODEX del progetto Eco Home

Documento preparato per Google Antigravity.

- Progetto analizzato: **Eco Home**
- Versione analizzata: **1.1.7**
- Data della revisione: **17 luglio 2026**
- Repository: `gates538/eco-home`
- Obiettivo: segnalare malfunzionamenti, rischi e miglioramenti consigliati prima di aggiungere nuove funzionalità

## Opinione generale

Eco Home è un progetto utile e già più curato di una normale automazione Home Assistant personale. La combinazione tra presenza e apertura del portone, la diagnostica persistente, gli scenari vocali, il ripristino del volume e la documentazione mostrano una buona attenzione all'uso reale.

La valutazione complessiva è **7/10**.

La struttura è valida, ma la versione 1.1.7 ha alcuni problemi operativi, soprattutto nella nuova gestione dei condizionatori, nelle notifiche con foto e nell'allineamento delle guide. Prima di sviluppare altre funzioni consiglio una versione **1.1.8 di consolidamento**.

## Controlli già eseguiti da CODEX

Sono stati eseguiti questi controlli locali:

- tutti e quattro i file YAML correnti vengono caricati correttamente da un parser YAML;
- tutti i 154 template Jinja individuati nell'automazione sono sintatticamente validi;
- tutti i collegamenti locali presenti nei file Markdown puntano a file esistenti;
- il repository locale era pulito durante la revisione;
- la release GitHub più recente risulta essere la 1.1.7.

Questi controlli confermano la validità sintattica, ma **non sostituiscono una prova su un'istanza Home Assistant reale** con le entità configurate.

---

## 1. Gestione non sicura del pulsante "Accendi condizionatori"

**Priorità: alta**

### Posizione

File `eco-home-v1.1.7.yaml`:

- trigger evento circa alle righe 60-64;
- gestione accensione circa alle righe 67-94;
- pulsanti delle notifiche circa alle righe 570-631.

### Comportamento attuale

Tutte le notifiche usano lo stesso identificatore statico:

```yaml
action: TURN_ON_AC
```

Quando Home Assistant riceve un evento `mobile_app_notification_action` con questo valore, accende i condizionatori senza ricontrollare:

- se Eco Home è ancora attivo;
- se la modalità silenziosa è attiva;
- se la temperatura è ancora superiore alla soglia;
- se la notifica è recente;
- se l'evento appartiene proprio alla notifica che ha generato la richiesta;
- quale telefono o utente ha premuto il pulsante.

### Malfunzionamento possibile

Una vecchia notifica rimasta sul telefono può essere premuta ore o giorni dopo e accendere comunque i condizionatori. L'azione può funzionare anche se nel frattempo Eco Home è stato disattivato.

Gli identificatori delle azioni sono inoltre condivisi fra tutte le notifiche Companion. La documentazione ufficiale consiglia di generarli in modo univoco usando il contesto dell'esecuzione.

Riferimento: <https://companion.home-assistant.io/docs/notifications/actionable-notifications/>

### Correzione richiesta

Separare la richiesta clima dal flusso principale di benvenuto e:

1. generare identificatori unici, per esempio usando `context.id`;
2. associare la risposta alla singola notifica;
3. applicare un timeout, consigliati 5-10 minuti;
4. prima dell'accensione verificare nuovamente che Eco Home sia attivo;
5. verificare che almeno un sensore di temperatura sia valido;
6. verificare nuovamente la temperatura;
7. verificare che la lista `ac_climate_entities` non sia vuota;
8. registrare chiaramente esito positivo, timeout, rifiuto o errore.

### Criteri di accettazione

- Una notifica scaduta non deve più accendere il clima.
- Una risposta appartenente a un'altra notifica non deve essere accettata.
- Con Eco Home disattivato il clima non deve accendersi.
- Se i sensori non sono disponibili, non deve essere proposta o eseguita l'accensione.
- Il pulsante "No, grazie" deve terminare correttamente il flusso senza lasciare esecuzioni in attesa.

---

## 2. Risposta del pulsante clima rallentata dalla coda TTS

**Priorità: alta**

### Posizione

Nel file `eco-home-v1.1.7.yaml` l'automazione usa:

```yaml
mode: queued
max: 5
max_exceeded: silent
```

Il flusso del TTS contiene inoltre un ritardo calcolato in base alla lunghezza del messaggio.

### Malfunzionamento

Se l'utente preme "Sì, accendi" mentre l'annuncio vocale è ancora in esecuzione, l'evento viene inserito nella stessa coda. L'accensione può quindi partire soltanto dopo la conclusione del TTS, del ritardo, del ripristino del volume e delle altre azioni.

In caso di più trigger, la coda può arrivare al limite di cinque esecuzioni. Poiché `max_exceeded` è impostato su `silent`, un evento ulteriore può essere perso senza una segnalazione evidente.

Riferimento: <https://www.home-assistant.io/docs/automation/modes/>

### Correzione richiesta

Creare un'automazione o uno script separato per la notifica interattiva del clima. Il flusso TTS può continuare a essere serializzato, mentre la risposta al pulsante deve poter essere elaborata immediatamente e indipendentemente.

### Criteri di accettazione

- Premendo il pulsante, la gestione deve partire entro pochi secondi anche mentre il Nest Hub sta parlando.
- L'elaborazione della risposta non deve attendere la coda TTS.
- Un eventuale errore nella gestione clima non deve interrompere o sporcare la diagnostica del benvenuto.

---

## 3. Snapshot della telecamera esposto tramite la cartella `www`

**Priorità: alta per privacy**

### Posizione

Nel file `eco-home-v1.1.7.yaml`:

```yaml
snapshot_file_path: /config/www/snapshots/eco_home_sala_2.jpg
snapshot_access_url: /local/snapshots/eco_home_sala_2.jpg
```

### Rischio

La cartella `www` viene pubblicata da Home Assistant tramite `/local`. È funzionale per gli allegati, ma non è la scelta migliore per una fotografia scattata da una telecamera interna: chi conosce l'URL può raggiungere il file senza l'autenticazione prevista per i contenuti media.

La documentazione Companion indica `media_source` come opzione raccomandata perché richiede intestazioni di autenticazione.

Riferimento: <https://companion.home-assistant.io/docs/notifications/notification-attachments/>

### Correzione richiesta

Usare preferibilmente:

```yaml
snapshot_file_path: /media/eco_home/eco_home_sala_2.jpg
snapshot_access_url: /media/local/eco_home/eco_home_sala_2.jpg
```

Aggiornare di conseguenza:

- automazione;
- `README.md`;
- `GUIDA_AGGIORNAMENTO.md`;
- `GUIDA_PERSONALIZZAZIONE.md`;
- `REQUISITI_HARDWARE.md`.

Valutare anche un nome univoco o un parametro anti-cache per evitare che notifiche successive mostrino una fotografia sovrascritta.

### Criteri di accettazione

- L'immagine deve essere visibile nell'app Companion autenticata.
- L'URL non deve rendere pubblica la fotografia senza autenticazione.
- Due rientri ravvicinati non devono mostrare in modo errato la stessa immagine memorizzata nella cache.

---

## 4. Notifiche duplicate con i valori predefiniti

**Priorità: medio-alta**

### Posizione

Nel file `eco-home-v1.1.7.yaml`:

```yaml
stefano_notification_service: notify.notify
laura_notification_service: notify.notify
```

Nel caso di rientro di coppia lo stesso servizio viene poi chiamato una volta per Stefano e una volta per Laura, sia per la foto sia per la richiesta di accensione del clima.

### Malfunzionamento

Con la configurazione pubblicata, i due servizi sono identici. In un rientro di coppia `notify.notify` viene quindi eseguito due volte e può inviare a tutti i dispositivi due notifiche uguali.

### Correzione richiesta

Gestire esplicitamente questi casi:

- se i due servizi sono diversi, inviare una notifica a ciascuno;
- se sono uguali, chiamare il servizio una sola volta;
- in alternativa, richiedere due servizi `notify.mobile_app_*` distinti e non usare `notify.notify` come valore predefinito;
- per più dispositivi, documentare un gruppo di notifica dedicato.

### Criteri di accettazione

- Ogni telefono deve ricevere una sola notifica per lo stesso evento.
- Il rientro di coppia deve funzionare sia con due servizi distinti sia con un solo gruppo condiviso.

---

## 5. Variabili configurabili non applicate realmente alle azioni

**Priorità: media**

### Problema

La sezione finale dichiara variabili come:

```yaml
speaker: media_player.nest_hub_sala
tts_engine: tts.google_ai_tts
light_entity: light.luceambiente
tv_media_player: media_player.tv_sala_ue85du7170uxzt
light_transition_seconds: 0
```

Tuttavia molte azioni continuano a usare direttamente gli entity ID originali. In particolare:

- `tts_engine` è dichiarato ma il target TTS è scritto direttamente;
- `light_entity` è dichiarato ma luce e condizione usano l'entity ID diretto;
- `speaker` viene usato per alcuni controlli, ma non per tutti i target;
- `tv_media_player` viene usato per leggere lo stato, ma le azioni di mute usano l'entity ID diretto;
- `light_transition_seconds` è dichiarato, ma nell'azione compare `transition: 0`;
- `project_name`, `dryer_power_sensor` e `last_announcement_ts` risultano inutilizzati.

### Conseguenza

Un utente può cambiare correttamente le variabili finali ma lasciare involontariamente le azioni puntate ai dispositivi di Stefano e Laura. La configurazione appare centralizzata, ma non lo è completamente.

### Correzione richiesta

Usare le variabili in tutti i target e in tutti i dati in cui Home Assistant permette i template. Gli entity ID dei trigger, che non sempre possono essere parametrizzati nello stesso modo, devono essere raccolti in una sezione chiaramente separata e documentata.

Rimuovere le variabili inutilizzate oppure implementarne davvero l'uso.

### Criteri di accettazione

- Cambiando `speaker` deve cambiare l'intero percorso audio.
- Cambiando `tv_media_player` devono cambiare controllo stato, mute e ripristino.
- Cambiando `light_entity` deve cambiare sia la condizione sia l'accensione.
- Non devono rimanere variabili dichiarate ma mai usate senza una spiegazione.

---

## 6. Diagnostica TTS potenzialmente falsa

**Priorità: media**

### Comportamento attuale

Le azioni `tts.speak` usano `continue_on_error: true`. Dopo il tentativo, il flusso continua e scrive esiti come:

```text
Annuncio completato
Test inviato al Nest Hub
```

### Malfunzionamento

Se `tts.speak` genera un errore, l'automazione può comunque arrivare a registrare un successo. Nel flusso reale può anche consumare il promemoria dell'asciugatrice pur senza avere riprodotto il messaggio.

La scelta di continuare è comprensibile perché consente di ripristinare TV e volume, ma la diagnostica non deve dichiarare che l'annuncio è stato completato con certezza.

### Correzione richiesta

Ristrutturare il percorso audio in modo che:

1. TV e volume vengano sempre ripristinati;
2. un errore TTS produca un esito distinto;
3. il promemoria asciugatrice venga cancellato solo dopo un esito ritenuto valido;
4. se non è possibile conoscere la riproduzione reale, usare una dicitura onesta come `Richiesta TTS inviata` invece di `Annuncio completato`.

### Criteri di accettazione

- Un errore del provider TTS non deve comparire come successo.
- Un errore non deve lasciare la TV muta o il volume modificato.
- Il promemoria asciugatrice non deve essere perso se il messaggio non è stato riprodotto.

---

## 7. La dashboard completa mostra in rosso anche gli esiti positivi

**Priorità: media**

### Posizione

File `eco-home-v1.1.7-dashboard-tuttacasa.yaml`, circa righe 183-188.

### Malfunzionamento

La dashboard considera positivo soltanto un testo che contiene la parola `successo`:

```jinja
{% if 'successo' in esito | lower %}
```

Gli esiti realmente prodotti dall'automazione usano invece testi come:

- `Annuncio completato: Stefano`;
- `Test inviato al Nest Hub: Laura`;
- `Condizionatori accesi da notifica`;
- `Promemoria asciugatrice salvato per il prossimo rientro`.

Questi esiti vengono quindi mostrati con indicatore rosso anche quando l'operazione è riuscita.

### Correzione richiesta

È preferibile non dedurre lo stato dal testo libero. Possibili soluzioni:

- aggiungere un helper strutturato con valori `ok`, `warning`, `error`, `idle`;
- oppure aggiornare temporaneamente la condizione includendo tutti gli esiti positivi previsti.

La prima soluzione è più stabile.

---

## 8. Le guide della versione corrente non sono allineate

**Priorità: medio-alta**

### Problemi trovati

1. `GUIDA_HELPER_UI.md` dichiara ancora Eco Home 1.1.4 e 14 helper.
2. La guida UI non contiene `input_boolean.eco_home_notifiche_foto`.
3. Il README dichiara invece correttamente 15 helper.
4. `GUIDA_CARD_TEST.md` indica ancora versione e nome file 1.1.4.
5. `GUIDA_DIAGNOSTICA.md` indica ancora la 1.1.4.
6. `GUIDA_PULSANTE_TEST.md` indica ancora la 1.1.4.
7. La descrizione interna di `eco-home-v1.1.7.yaml` riporta `Eco home v1.1.6`.
8. `DIPENDENZE.md` e `REQUISITI_HARDWARE.md` contengono ancora riferimenti alla logica della 1.1.4.

### Conseguenza concreta

Una nuova installazione eseguita tramite la guida UI crea 14 helper anziché 15. L'helper per le notifiche fotografiche manca e la funzione rimane disattivata o non configurata correttamente.

### Correzione richiesta

Allineare tutte le guide alla versione 1.1.8 e introdurre un controllo automatico che cerchi riferimenti a versioni precedenti nei file correnti, escludendo `CHANGELOG.md` e `archive/`.

---

## 9. Il test indicato per gli snapshot non prova la funzione fotografica

**Priorità: media**

### Posizione

In `GUIDA_AGGIORNAMENTO.md`, la sezione di verifica suggerisce di eseguire `Percorso audio` o `Rientro Stefano` dal pulsante di test e poi controllare lo snapshot e la notifica.

### Malfunzionamento

Il trigger `manual_test` esegue soltanto il percorso vocale. Non raggiunge il blocco del rientro reale che contiene `camera.snapshot` e le notifiche fotografiche. Di conseguenza il test descritto non può produrre la fotografia.

### Correzione richiesta

Scegliere una delle due soluzioni:

1. aggiungere uno scenario esplicito `Test notifica con foto`, chiaramente separato dalla presenza reale;
2. correggere la guida spiegando che la verifica fotografica richiede un test manuale dell'azione `camera.snapshot` e del servizio `notify.mobile_app_*`.

Il test non deve simulare un rientro reale alterando gli helper diagnostici senza dichiararlo.

---

## 10. Metadati di progetto e processo di pubblicazione

**Priorità: media per un progetto pubblico**

### Licenza assente

Nel repository non è presente un file `LICENSE`. Un repository pubblico senza licenza può essere visualizzato e sottoposto a fork tramite GitHub, ma non concede chiaramente il diritto di usare, modificare e distribuire il progetto.

Riferimento: <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository>

Scegliere consapevolmente una licenza. Per un'automazione condivisibile si possono valutare, per esempio, MIT o Apache-2.0, ma la scelta finale appartiene al proprietario del progetto.

### Controlli automatici assenti

Non è presente una cartella `.github/workflows`. Si consiglia una piccola pipeline che controlli:

- parsing dei file YAML;
- sintassi dei template Jinja, nei limiti di un controllo statico;
- collegamenti Markdown locali;
- numero e nomi degli helper;
- coerenza della versione corrente;
- assenza di vecchi nomi `echo_home_*` nei file correnti;
- corrispondenza fra file elencati nel README e file realmente pubblicati.

---

## Miglioramenti consigliati ma non bloccanti

### Rendere configurabile la soglia clima

Il valore `26.0` è ripetuto direttamente nella logica. Introdurre una variabile, per esempio:

```yaml
ac_offer_temperature_threshold: 26.0
```

### Non forzare l'arresto del TTS soltanto con una stima temporale

Il tempo di riproduzione viene stimato dalla lunghezza del testo. Una risposta lenta del provider può causare un `media_stop` anticipato. Valutare un'attesa basata sullo stato del lettore con timeout di sicurezza, verificando prima il comportamento reale del Nest Hub.

### Gestire meglio l'identità delle persone

La configurazione contiene ancora riferimenti diretti a `person.stefano` e `person.laura` in vari template. Per rendere il progetto riutilizzabile sarebbe utile centralizzare anche la mappatura fra persona, nome, nomignoli e servizio di notifica.

### Rendere generica la plancia "Tutta Casa"

La dashboard contiene dati personali come `STEFANO'S COMMAND CENTER` e `Borgo Santa Maria, Roma`. Se il file è destinato al pubblico, questi valori devono essere indicati chiaramente come esempi da personalizzare oppure sostituiti da testi generici.

La griglia fissa a tre colonne può inoltre risultare stretta su smartphone; verificare il layout mobile.

### Evitare una fotografia esterna non necessaria

La plancia usa un'immagine Unsplash come immagine di base della camera. Questo crea una dipendenza esterna e una richiesta di rete non indispensabile. Valutare un asset locale o la sola immagine della telecamera.

---

## Aspetti positivi da conservare

Durante la correzione non devono andare persi questi comportamenti:

- conferma del rientro in entrambi gli ordini `persona → portone` e `portone → persona`;
- esclusione degli stati iniziali `unknown` e `unavailable`;
- cooldown contro annunci duplicati;
- modalità silenziosa;
- test vocale indipendente dalla presenza reale;
- salvataggio e ripristino del volume del Nest Hub;
- rispetto di una TV già muta prima dell'annuncio;
- mancata cancellazione del promemoria asciugatrice durante i test vocali;
- diagnostica persistente anche con `debug: false`;
- archivio delle release precedenti;
- documentazione separata per hardware, dipendenze e personalizzazione.

Le modifiche devono riguardare i file correnti. Le cartelle sotto `archive/` devono restare copie fedeli delle versioni pubblicate in passato.

---

## Ordine di lavoro consigliato per Antigravity

1. Separare il gestore della risposta clima dal flusso TTS.
2. Rendere uniche e temporanee le azioni delle notifiche.
3. Aggiungere tutte le condizioni di sicurezza prima di accendere i climatizzatori.
4. Spostare gli snapshot da `/www` a `/media`.
5. Eliminare le notifiche duplicate.
6. Centralizzare realmente speaker, TTS, TV, luce e altri entity ID.
7. Correggere la diagnostica TTS e il colore degli esiti.
8. Creare un test reale per foto e notifiche.
9. Allineare tutta la documentazione e i metadati alla 1.1.8.
10. Aggiungere licenza e controlli automatici.

## Verifica finale richiesta

Prima di pubblicare la correzione, eseguire almeno questi scenari:

| Scenario | Risultato atteso |
|---|---|
| Persona passa a `home`, poi si apre il portone | Un solo benvenuto |
| Portone aperto, poi persona passa a `home` | Un solo benvenuto |
| Due persone rientrano insieme | Profilo coppia e una notifica per telefono |
| Persona era assente da meno del minimo | Nessun benvenuto |
| Eco Home disattivato | Nessun annuncio e nessuna accensione clima |
| Modalità silenziosa attiva | Nessun TTS automatico |
| Temperatura sotto soglia | Nessuna richiesta di accensione clima |
| Temperatura sopra soglia | Richiesta interattiva corretta |
| Pressione immediata su "Sì" durante il TTS | Risposta elaborata senza attendere il TTS |
| Pressione su una vecchia notifica | Nessuna accensione |
| Sensori temperatura non disponibili | Nessuna proposta clima e diagnostica chiara |
| Lista clima vuota o non valida | Nessun errore non gestito |
| Servizi di notifica uguali | Nessun duplicato |
| Casa già occupata | Nessuna foto di rientro, come previsto |
| Errore `camera.snapshot` | TTS ancora funzionante e diagnostica corretta |
| Errore `tts.speak` | TV e volume ripristinati, nessun falso successo |
| Test fotografico | Snapshot e notifica realmente prodotti |
| Visualizzazione mobile dashboard | Layout leggibile senza tre colonne compresse |

## Risultato atteso della versione di consolidamento

La versione successiva dovrebbe mantenere tutte le funzioni della 1.1.7, ma con:

- risposte clima immediate, uniche e con scadenza;
- nessuna possibilità di accensione da notifiche vecchie;
- fotografie protette da autenticazione;
- nessuna notifica duplicata;
- configurazione realmente centralizzata;
- diagnostica coerente con il risultato effettivo;
- documentazione completamente allineata;
- test ripetibili e controlli automatici di base.

Questa revisione non richiede di riscrivere l'intero progetto. La base è buona: serve soprattutto consolidare i flussi aggiunti nelle ultime release e ridurre le incoerenze introdotte dalla crescita rapida del file principale.
