# Creazione degli helper Eco Home dalla UI

Eco Home 1.1.8 utilizza 15 helper con prefisso `eco_home_*`.

Vai in **Impostazioni → Dispositivi e servizi → Helper → Crea helper**.

Se possiedi già helper `echo_home_*`, non crearne altri: segui
[GUIDA_AGGIORNAMENTO.md](GUIDA_AGGIORNAMENTO.md) e rinomina gli Entity ID.

## Interruttori

| Nome | Entity ID | Icona |
|---|---|---|
| Eco Home attivo | `input_boolean.eco_home_attivo` | `mdi:home-assistant` |
| Eco Home silenzioso | `input_boolean.eco_home_silenzioso` | `mdi:volume-off` |
| Eco Home asciugatrice da annunciare | `input_boolean.eco_home_asciugatrice_da_annunciare` | `mdi:tumble-dryer-alert` |
| Eco Home notifiche foto | `input_boolean.eco_home_notifiche_foto` | `mdi:camera` |

Al termine imposta **Eco Home attivo** su ON e lascia gli altri su OFF.

## Data e ora

Per tutti abilita sia **Data** sia **Ora**.

| Nome | Entity ID |
|---|---|
| Eco Home asciugatrice fine | `input_datetime.eco_home_asciugatrice_fine` |
| Eco Home ultimo annuncio | `input_datetime.eco_home_ultimo_annuncio` |
| Eco Home ultima apertura portone | `input_datetime.eco_home_ultima_apertura_portone` |
| Eco Home ultimo arrivo | `input_datetime.eco_home_ultimo_arrivo` |

## Pulsante

| Nome | Entity ID | Icona |
|---|---|---|
| Eco Home test vocale | `input_button.eco_home_test_vocale` | `mdi:account-voice` |

## Menu a tendina

Nome: **Eco Home scenario di test**

Entity ID: `input_select.eco_home_scenario_test`

Icona: `mdi:test-tube`

Inserisci le opzioni nello stesso ordine:

```text
Percorso audio
Rientro Stefano
Rientro Laura
Rientro di coppia
Modalità notte
Promemoria asciugatrice
```

## Testi diagnostici

Lascia valore iniziale e pattern vuoti. Usa la modalità testo.

| Nome | Entity ID | Massimo | Icona |
|---|---|---:|---|
| Eco Home ultimo evento | `input_text.eco_home_ultimo_evento` | 255 | `mdi:timeline-clock-outline` |
| Eco Home ultimo esito | `input_text.eco_home_ultimo_esito` | 255 | `mdi:check-decagram-outline` |
| Eco Home ultimo profilo | `input_text.eco_home_ultimo_profilo` | 100 | `mdi:account-tag-outline` |
| Eco Home ultimo messaggio | `input_text.eco_home_ultimo_messaggio` | 255 | `mdi:message-text-outline` |
| Eco Home ultima persona | `input_text.eco_home_ultima_persona` | 100 | `mdi:account-clock-outline` |

## Controllo finale

In **Strumenti per sviluppatori → Stati**, cerca `eco_home`. Devono comparire
15 helper e nessun Entity ID deve terminare con `_2` o `_3`.

