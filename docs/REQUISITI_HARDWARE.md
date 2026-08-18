# Requisiti hardware e compatibilità di Eco Home v1.1.8

Questa guida descrive i dispositivi fisici necessari per usare Eco Home e le
funzioni che devono esporre in Home Assistant.

Non è una lista obbligatoria di marche o modelli. Un prodotto è compatibile
soltanto se, dopo essere stato integrato in Home Assistant, crea le entità e
supera le prove indicate in questa guida.

Per l'elenco degli entity ID, degli helper e delle integrazioni software consulta
anche [DIPENDENZE.md](DIPENDENZE.md).

## Configurazione minima

Per il benvenuto vocale al rientro servono:

| Componente fisico | Entità in Home Assistant | Requisito essenziale |
|---|---|---|
| Un sistema che esegue Home Assistant | — | Deve rimanere acceso e raggiungibile dalla rete locale |
| Un dispositivo di presenza per ogni persona | `person.*` tramite uno o più `device_tracker.*` | La persona deve passare da `not_home` a `home` |
| Un sensore magnetico sul portone | `binary_sensor.*` | `off` a portone chiuso e `on` a portone aperto |
| Un altoparlante o display compatibile TTS | `media_player.*` | Deve riprodurre realmente l'azione `tts.speak` |
| Una rete locale funzionante | — | Home Assistant e lettore TTS devono comunicare tra loro |

Gli helper `input_boolean`, `input_datetime`, `input_button`, `input_select` e
`input_text` sono software: non richiedono altro hardware.

La luce, la TV e i sensori dell'asciugatrice sono opzionali. Senza questi
dispositivi si perde soltanto la relativa funzione.

### Tre configurazioni fisiche di esempio

Questi esempi aiutano a capire cosa occorre materialmente. Non sono pacchetti
commerciali né garanzie di compatibilità automatica.

| Situazione | Componenti fisici |
|---|---|
| Riutilizzo dell'impianto esistente | Home Assistant già installato, uno smartphone per persona, Nest Hub già presente e un sensore del portone compatibile con un'integrazione già attiva |
| Nuovo sensore Zigbee | Componenti precedenti più un contatto Zigbee, per esempio SONOFF SNZB-04P, e un coordinatore Zigbee compatibile se ancora assente |
| Nuovo sensore Matter/Thread | Componenti precedenti più un contatto Matter over Thread, per esempio Aqara Door and Window Sensor P2, e un Thread Border Router se ancora assente |

Non è necessario comprare sia il coordinatore Zigbee sia il Thread Border
Router: serve soltanto l'infrastruttura richiesta dalla tecnologia del sensore
scelto.

## 1. Sistema Home Assistant

Eco Home non richiede un modello preciso. Può funzionare, per esempio, su:

- Home Assistant Green o Yellow;
- Raspberry Pi adeguatamente configurato;
- mini PC o computer sempre acceso;
- macchina virtuale, server o NAS supportato dalla propria installazione.

Il sistema deve essere affidabile e sempre acceso. Il sensore del portone, il
telefono e il lettore TTS devono aggiornare Home Assistant senza ritardi
anomali.

Un adattatore radio aggiuntivo serve solo se il sensore scelto usa una rete che
non è già disponibile nell'impianto, per esempio Zigbee o Z-Wave.

## 2. Sensore di apertura del portone

### Requisiti obbligatori

Il sensore deve creare un'entità del dominio `binary_sensor`, per esempio:

```text
binary_sensor.porta_contact
```

Eco Home usa questa corrispondenza:

| Situazione reale | Stato tecnico richiesto |
|---|---|
| Portone chiuso | `off` |
| Portone aperto | `on` |

La dicitura grafica può essere **Aperto/Chiuso**, ma in **Strumenti per
sviluppatori → Stati** i valori tecnici devono essere `on` e `off`. È
consigliata la classe dispositivo `door` o `opening`.

L'automazione ignora correttamente i passaggi provenienti da `unknown` o
`unavailable`. Di conseguenza il sensore deve rimanere disponibile e produrre
un vero passaggio `off` → `on` quando il portone viene aperto.

### Tipi di sensore utilizzabili

| Tecnologia | Esempi indicativi | Hardware aggiuntivo | Nota pratica |
|---|---|---|---|
| Zigbee | [SONOFF SNZB-04P](https://sonoff.tech/products/sonoff-zigbee-door-window-sensor-snzb-04p), IKEA PARASOLL se già posseduto e altri contatti Zigbee | Coordinatore Zigbee compatibile, se non già presente | Soluzione a batteria e locale; verificare sempre il modello con ZHA o con il proprio gateway |
| Matter over Thread | [Aqara Door and Window Sensor P2](https://www.aqara.com/us/product/door-and-window-sensor-p2/) e altri contatti Matter/Thread | Thread Border Router | Non basta la sola integrazione Matter: il dispositivo Thread richiede anche il border router |
| Z-Wave | Sensore porta/finestra Z-Wave compatibile | Adattatore Z-Wave e integrazione Z-Wave | Controllare frequenza europea e compatibilità prima dell'acquisto |
| Wi-Fi o LAN | Sensore o modulo a contatto integrato localmente | Normalmente nessun coordinatore radio dedicato | Verificare autonomia, rapidità e dipendenza eventuale dal cloud |
| Impianto esistente | Contatto di allarme, ESPHome, MQTT o ponte del citofono | Dipende dall'impianto | È valido se genera un `binary_sensor` stabile; i collegamenti elettrici devono essere realizzati in sicurezza |

Gli esempi sono famiglie di dispositivi da valutare, non una garanzia universale:
firmware, gateway e integrazione scelta possono cambiare le entità disponibili.

Con Zigbee, l'integrazione [ZHA](https://www.home-assistant.io/integrations/zha/)
richiede un coordinatore compatibile. Per un dispositivo Matter basato su
Thread serve un [Thread Border Router](https://www.home-assistant.io/integrations/thread/);
la documentazione [Matter](https://www.home-assistant.io/integrations/matter/)
riporta, tra gli esempi, Nest Hub di seconda generazione, HomePod mini e Home
Assistant Connect ZBT-1/ZBT-2 insieme all'app OpenThread Border Router. Un Nest
Hub di prima generazione non va quindi considerato automaticamente un border
router. Una radio Home Assistant configurata per Zigbee non deve essere
considerata automaticamente disponibile anche per Thread: controlla la
configurazione radio prima di acquistare il sensore.

### Installazione fisica

- Fissa il corpo del sensore e il magnete rispettando la distanza massima
  dichiarata dal produttore.
- Evita che vibrazioni o giochi del portone producano aperture fantasma.
- Controlla che il sensore torni a `off` quando il portone viene chiuso.
- Verifica batteria e qualità del collegamento radio.
- Se il portone è condominiale, ottieni le autorizzazioni necessarie prima di
  fissare o collegare qualsiasi dispositivo.

### Prova obbligatoria

1. Apri **Strumenti per sviluppatori → Stati**.
2. Cerca il `binary_sensor` scelto.
3. Apri e chiudi fisicamente il portone almeno cinque volte.
4. Verifica ogni volta il passaggio immediato `off` → `on` → `off`.
5. Controlla che non compaiano `unknown` o `unavailable`.

## 3. Rilevamento della presenza

Non è necessario acquistare un sensore di presenza separato se ogni persona ha
uno smartphone con l'app Home Assistant Companion configurata correttamente.
L'app crea normalmente un `device_tracker.*`, da associare alla corrispondente
entità `person.*`.

Il file pubblicato è configurato per:

```text
person.stefano
person.laura
```

Per ogni persona è necessario:

- uno smartphone o un altro tracker affidabile;
- un'entità `person.*` associata al tracker;
- accesso remoto funzionante quando si è fuori casa;
- localizzazione in background autorizzata;
- stato `not_home` durante l'assenza e `home` al rientro.

L'app Companion e il GPS sono preferibili come fonte principale. Il solo
tracker del router può segnalare `home` già dal parcheggio, perché il Wi-Fi può
raggiungere l'esterno. Questo non avvia da solo il benvenuto: Eco Home richiede
anche l'apertura del portone entro cinque minuti.

Home Assistant può combinare più tracker nella stessa persona. I tracker di
connessione possono avere priorità quando indicano `home`; il comportamento è
spiegato nella documentazione dell'integrazione
[Person](https://www.home-assistant.io/integrations/person/). Le autorizzazioni
e gli aggiornamenti in background sono descritti nella guida
[Location dell'app Companion](https://companion.home-assistant.io/docs/core/location/).

### Prova obbligatoria

1. Allontanati abbastanza da ottenere `not_home`.
2. Mantieni l'assenza per almeno due minuti, come richiesto dalla configurazione
   predefinita di Eco Home.
3. Rientra e osserva in **Strumenti per sviluppatori → Stati** quando la persona
   passa a `home`.
4. Apri il portone entro cinque minuti dal cambio di presenza.
5. Ripeti anche la prova inversa: portone aperto prima e persona `home` entro i
   cinque minuti successivi.

Se il passaggio a `home` avviene più di cinque minuti prima dell'apertura del
portone, aumenta con cautela `arrival_person_door_window_seconds` seguendo
[GUIDA_PERSONALIZZAZIONE.md](GUIDA_PERSONALIZZAZIONE.md).

## 4. Altoparlante o display per il TTS

### Requisiti obbligatori

Il dispositivo deve creare un'entità `media_player.*` e deve riprodurre davvero
un messaggio inviato con `tts.speak`. La sola presenza dell'entità non dimostra
la compatibilità.

Per il funzionamento completo sono consigliate anche queste capacità:

- regolazione tramite `media_player.volume_set`;
- attributo `volume_level`, per salvare e ripristinare il volume;
- arresto tramite `media_player.media_stop`;
- riproduzione di un URL audio generato dal provider TTS.

Eco Home usa un'entità TTS distinta dal lettore:

```text
tts.google_ai_tts
media_player.nest_hub_sala
```

Il provider `tts.*` è una dipendenza software. L'altoparlante o display è il
dispositivo hardware che deve riprodurre l'audio.

### Esempi indicativi

| Dispositivo | Integrazione tipica | Valutazione per Eco Home |
|---|---|---|
| Google Nest Hub, Nest Mini o Google Home | Google Cast | Scelta consigliata da provare; il Nest Hub è la configurazione di riferimento già verificata |
| Chromecast o Chromecast Audio collegato a un impianto audio | Google Cast | Possibile, se il relativo `media_player` supera tutti i test |
| Sonos o IKEA Symfonisk | Sonos | Possibile, ma da verificare: il flusso corrente può interrompere l'audio già in riproduzione |
| Smart TV o soundbar | Integrazione del produttore | Non presumerne la compatibilità: molte entità non accettano `play_media` o non riproducono il formato TTS |
| Amazon Echo | Integrazioni non standard | Non supportato direttamente dal pacchetto standard; richiede una soluzione aggiuntiva e una personalizzazione |

Nelle prove effettuate durante lo sviluppo, una Samsung Ultra Slim Soundbar non
supportava `media_player.play_media`; una TV Samsung esponeva funzioni
multimediali ma non riproduceva il TTS. Per questo la guida richiede una prova
reale e non si basa soltanto sul nome del prodotto o su `supported_features`.

Google Cast deve poter raggiungere l'audio generato da Home Assistant tramite
HTTP o HTTPS. Se il TTS non parte, controlla l'URL interno in **Impostazioni →
Sistema → Rete**, la raggiungibilità tra le reti e l'eventuale isolamento dei
client Wi-Fi. La documentazione ufficiale di
[Google Cast](https://www.home-assistant.io/integrations/cast/) spiega anche i
limiti di DNS, mDNS e sottoreti.

### Prova TTS obbligatoria

In **Strumenti per sviluppatori → Azioni**, adatta e prova:

```yaml
action: tts.speak
target:
  entity_id: tts.google_ai_tts
data:
  media_player_entity_id: media_player.nest_hub_sala
  message: "Prova audio Eco Home completata."
  cache: false
```

La sintassi dell'azione è descritta nella documentazione
[Speak di Home Assistant](https://www.home-assistant.io/actions/tts.speak/).

Poi prova la regolazione del volume:

```yaml
action: media_player.volume_set
target:
  entity_id: media_player.nest_hub_sala
data:
  volume_level: 0.4
```

Infine prova l'arresto:

```yaml
action: media_player.media_stop
target:
  entity_id: media_player.nest_hub_sala
```

Se il primo test non produce una voce udibile, quel dispositivo non deve essere
indicato come lettore TTS di Eco Home finché il problema non è stato risolto.

## 5. Luce opzionale

La funzione di accensione serale usa:

```text
light.luceambiente
sun.sun
```

La luce deve accettare `light.turn_on`. Il file corrente invia anche:

- `brightness_pct`;
- `color_temp_kelvin`;
- `transition`.

Per mantenere tutti gli effetti serve quindi una luce dimmerabile con
temperatura colore. Una semplice luce on/off può essere usata soltanto dopo
aver rimosso dal blocco dell'azione i parametri che non supporta.

`sun.sun` è un'entità software fornita dall'integrazione Sun e viene usata per
accendere la luce soltanto quando il sole è sotto l'orizzonte.

## 6. TV opzionale

Per abbassare temporaneamente l'audio durante il benvenuto, la TV o il relativo
ricevitore deve:

- creare un'entità `media_player.*`;
- supportare `media_player.volume_mute` sia con `true` sia con `false`;
- esporre correttamente l'attributo `is_volume_muted`;
- aggiornare lo stato quando è accesa o sta riproducendo.

Prova prima il mute e subito dopo il ripristino:

```yaml
action: media_player.volume_mute
target:
  entity_id: media_player.tv_sala_ue85du7170uxzt
data:
  is_volume_muted: true
```

Ripeti con `is_volume_muted: false`. Se il dispositivo non supporta l'azione,
imposta `tv_ducking_enabled: false` nell'automazione.

La TV non deve supportare il TTS: in Eco Home viene usata soltanto per il mute
temporaneo.

## 7. Asciugatrice opzionale

Non serve un modello specifico di asciugatrice. Serve un'integrazione che
esponga sensori utilizzabili da Home Assistant.

| Entità | Funzione | Necessità per il promemoria |
|---|---|---|
| `sensor.esterno_asciugatrice_machine_state` | Stato del ciclo | Necessaria |
| `sensor.esterno_asciugatrice_completion_time` | Orario previsto di fine | Opzionale, aggiunge il tempo residuo al saluto |
| `sensor.esterno_asciugatrice_energia_elettrica` | Consumo elettrico | Predisposta, ma non usata dalla logica della v1.1.8 |

Lo stato macchina deve passare da uno stato di lavoro a uno di questi valori
riconosciuti:

```text
off, idle, stop, stopped, complete, completed,
finish, finished, end, ended, none, standby
```

Lo stato finale deve rimanere stabile per due minuti. Se l'integrazione usa
parole diverse, aggiorna sia il trigger sia `dryer_finished_states` nel file
dell'automazione.

Il sensore dell'orario di completamento deve restituire una data/ora che Home
Assistant sappia convertire in timestamp.

## 8. Telecamera opzionale per notifiche foto

Per scattare e inviare una foto del rientro sul cellulare (se la casa era vuota):

* **Telecamera compatibile**: Deve supportare l'azione `camera.snapshot`. Puoi verificarla in **Strumenti per sviluppatori → Azioni**.
* **Cartella snapshot locale**: Devi creare la cartella `/media/eco_home/` sul tuo Home Assistant. L'immagine temporanea verrà salvata lì (es. `/media/eco_home/eco_home_sala_2.jpg`) e sarà accessibile all'app Companion o a Telegram tramite l'URL `/media/local/eco_home/eco_home_sala_2.jpg`.
* **Servizio di Notifica**: I telefoni devono avere configurata l'app Home Assistant Companion o l'integrazione di Telegram.

## 9. Sensori di temperatura e condizionatori (Clima) opzionali

Per abilitare l'annuncio vocale della temperatura interna e l'accensione intelligente del condizionatore:

* **Sensori di temperatura**: Devono essere entità che restituiscono un valore numerico (es. `sensor.*_temperature` o `sensor.*_temperatura`). Puoi configurare più sensori: l'automazione ne calcolerà la media matematica automaticamente.
* **Entità condizionatori (clima)**: Devono essere entità di tipo `climate.*` compatibili con le azioni `climate.turn_on` e `climate.set_hvac_mode` (impostati su `cool`).
* **Notifiche Push sul Cellulare**: I cellulari devono supportare le notifiche push interattive (actionable notifications) tramite l'app Home Assistant Companion per consentire la risposta sul pulsante "Sì, accendi".

## 10. Verifica finale di compatibilità

Prima di considerare pronto l'impianto, completa questa lista:

- [ ] Home Assistant rimane acceso ed è raggiungibile.
- [ ] Ogni `person.*` passa da `not_home` a `home` in modo affidabile.
- [ ] Il sensore del portone passa da `off` a `on` senza stati intermedi non validi.
- [ ] Il messaggio `tts.speak` viene riprodotto realmente.
- [ ] Il volume del lettore TTS può essere regolato e ripristinato.
- [ ] La rete permette al lettore di raggiungere l'audio TTS.
- [ ] La luce opzionale accetta luminosità e temperatura colore, oppure il blocco è stato adattato.
- [ ] La TV opzionale esegue mute e unmute, oppure `tv_ducking_enabled` è `false`.
- [ ] Lo stato opzionale dell'asciugatrice usa valori riconosciuti.
- [ ] La telecamera opzionale supporta l'azione `camera.snapshot`.
- [ ] La cartella locale `/media/eco_home/` è stata creata.
- [ ] I condizionatori e i sensori di temperatura opzionali sono configurati.
- [ ] Tutti gli entity ID sono stati sostituiti anche nella card e nelle azioni, non solo nelle variabili finali.

Soltanto dopo queste prove esegui il test **Percorso audio** dalla card e poi un
rientro reale. Per interpretare eventuali errori consulta
[GUIDA_DIAGNOSTICA.md](GUIDA_DIAGNOSTICA.md).

## Riferimenti ufficiali

- [Binary sensor: significato di `door` e `opening`](https://developers.home-assistant.io/docs/core/entity/binary-sensor/)
- [Person e priorità dei device tracker](https://www.home-assistant.io/integrations/person/)
- [Localizzazione dell'app Companion](https://companion.home-assistant.io/docs/core/location/)
- [Azione TTS Speak](https://www.home-assistant.io/actions/tts.speak/)
- [Integrazione Google Cast](https://www.home-assistant.io/integrations/cast/)
- [Integrazione Sonos](https://www.home-assistant.io/integrations/sonos/)
- [Zigbee Home Automation](https://www.home-assistant.io/integrations/zha/)
- [Matter](https://www.home-assistant.io/integrations/matter/)
- [Thread](https://www.home-assistant.io/integrations/thread/)
- [Z-Wave](https://www.home-assistant.io/integrations/zwave_js/)
