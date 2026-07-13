# Aggiornamento a Eco Home 1.1.4

La 1.1.4 corregge il prefisso storico `echo_home_*` e usa ovunque
`eco_home_*`. La logica dell'automazione non cambia.

Questa procedura conserva tutte le altre automazioni presenti in
`automations.yaml`.

## 1. Crea un backup

Da **Impostazioni → Sistema → Backup**, crea un backup. Copia inoltre
`/config/automations.yaml` e l'eventuale vecchio package degli helper in un
posto sicuro.

## 2. Migra gli helper

### Helper creati dalla UI

Vai in **Impostazioni → Dispositivi e servizi → Entità**. Cerca `echo_home` e
rinomina gli Entity ID sostituendo soltanto il prefisso:

```text
input_boolean.echo_home_attivo                         → input_boolean.eco_home_attivo
input_boolean.echo_home_silenzioso                     → input_boolean.eco_home_silenzioso
input_boolean.echo_home_asciugatrice_da_annunciare     → input_boolean.eco_home_asciugatrice_da_annunciare
input_datetime.echo_home_asciugatrice_fine             → input_datetime.eco_home_asciugatrice_fine
input_datetime.echo_home_ultimo_annuncio               → input_datetime.eco_home_ultimo_annuncio
input_datetime.echo_home_ultima_apertura_portone       → input_datetime.eco_home_ultima_apertura_portone
input_datetime.echo_home_ultimo_arrivo                 → input_datetime.eco_home_ultimo_arrivo
input_button.echo_home_test_vocale                     → input_button.eco_home_test_vocale
input_select.echo_home_scenario_test                   → input_select.eco_home_scenario_test
input_text.echo_home_ultimo_evento                     → input_text.eco_home_ultimo_evento
input_text.echo_home_ultimo_esito                      → input_text.eco_home_ultimo_esito
input_text.echo_home_ultimo_profilo                    → input_text.eco_home_ultimo_profilo
input_text.echo_home_ultimo_messaggio                  → input_text.eco_home_ultimo_messaggio
input_text.echo_home_ultima_persona                    → input_text.eco_home_ultima_persona
```

Non ricreare gli helper: rinominandoli conservi stato e impostazioni.

### Helper definiti tramite package YAML

1. Rimuovi o rinomina il vecchio file package che definisce `echo_home_*`.
2. Copia `eco-home-v1.1.4-helpers.yaml` in `/config/packages/`.
3. Non caricare contemporaneamente il vecchio e il nuovo package.

## 3. Sostituisci soltanto Eco Home

Apri `/config/automations.yaml` e cerca:

```yaml
- id: '1783777716602'
  alias: Eco home
```

Sostituisci esclusivamente quel blocco con il contenuto di
`eco-home-v1.1.4.yaml`. Non sostituire l'intero file se contiene altre
automazioni.

## 4. Aggiorna la card

Sostituisci la vecchia card con il contenuto di
`eco-home-v1.1.4-dashboard-card.yaml`.

## 5. Verifica

1. Esegui **Controlla configurazione**.
2. Riavvia Home Assistant se gli helper provengono da un package; altrimenti
   ricarica le automazioni.
3. In **Strumenti per sviluppatori → Stati**, cerca `echo_home`: non deve
   restare alcun helper attivo con quel prefisso.
4. Cerca `eco_home`: devono comparire tutti i 14 helper.
5. Apri la card, seleziona `Percorso audio` ed esegui il test.
6. Controlla `input_text.eco_home_ultimo_esito`.

## Ripristino

In caso di errore, ripristina `automations.yaml` e il package degli helper dal
backup. La versione 1.1.3 resta disponibile in `archive/v1.1.3`.
