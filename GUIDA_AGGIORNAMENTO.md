# Aggiornamento da Eco Home 1.1.2 a 1.1.3

Questa procedura conserva tutte le altre automazioni presenti in `automations.yaml`.

## 1. Crea un backup

Da **Impostazioni → Sistema → Backup**, crea un backup prima di modificare i file. Copia inoltre `/config/automations.yaml` in un posto sicuro.

## 2. Installa soltanto i nuovi helper

Se possiedi già gli helper della 1.1.2, usa come riferimento:

```text
eco-home-v1.1.3-helper-update.yaml
```

Puoi copiarlo in `/config/packages/` se i vecchi helper sono anch'essi definiti tramite package. Se invece li hai creati dalla UI, crea dalla UI soltanto questi nuovi helper:

```text
input_datetime.echo_home_ultima_apertura_portone
input_datetime.echo_home_ultimo_arrivo
input_select.echo_home_scenario_test
input_text.echo_home_ultimo_evento
input_text.echo_home_ultimo_esito
input_text.echo_home_ultimo_profilo
input_text.echo_home_ultimo_messaggio
input_text.echo_home_ultima_persona
```

Non creare due volte helper con lo stesso entity ID.

## 3. Sostituisci soltanto Eco Home

Apri `/config/automations.yaml` e cerca:

```yaml
- id: '1783777716602'
  alias: Eco home
```

Elimina esclusivamente quel blocco completo, fino alla riga precedente all'automazione successiva. Al suo posto incolla tutto il contenuto di:

```text
eco-home-v1.1.3.yaml
```

Non sostituire l'intero `automations.yaml`: le altre automazioni devono restare invariate.

## 4. Riporta le personalizzazioni

Confronta la vecchia automazione e riporta soltanto i tuoi entity ID, tempi e volumi. Consulta [GUIDA_PERSONALIZZAZIONE.md](GUIDA_PERSONALIZZAZIONE.md).

## 5. Aggiorna la card

Sostituisci il codice della vecchia card con:

```text
eco-home-v1.1.3-dashboard-card.yaml
```

## 6. Verifica

1. Esegui **Controlla configurazione**.
2. Ricarica automazioni e helper oppure riavvia Home Assistant.
3. Apri la card.
4. Seleziona `Percorso audio`.
5. Avvia il test e controlla `Ultimo esito`.
6. Verifica che il volume del Nest Hub torni al valore precedente.

## Ripristino

In caso di errore, ripristina il backup di `automations.yaml` e rimuovi soltanto gli helper nuovi della 1.1.3. La versione 1.1.2 resta disponibile in `archive/v1.1.2`.

