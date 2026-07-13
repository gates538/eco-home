# Guida agli scenari di test

Eco Home 1.1.4 usa:

```text
input_select.eco_home_scenario_test
input_button.eco_home_test_vocale
```

## Scenari disponibili

| Scenario | Cosa verifica |
|---|---|
| Percorso audio | TTS, Nest Hub, volume e TV |
| Rientro Stefano | Nomignoli e frasi maschili |
| Rientro Laura | Nomignoli e frasi femminili |
| Rientro di coppia | Nomignoli e frasi di coppia |
| Modalità notte | Frasi notturne e volume ridotto |
| Promemoria asciugatrice | Testo del promemoria senza modificare quello reale |

## Utilizzo dalla card

1. Apri la card Eco Home.
2. In **Scenario di test**, scegli il messaggio da simulare.
3. Premi **Avvia il test selezionato**.
4. Controlla la sezione **Diagnostica**.

Il test:

- funziona anche se gli annunci automatici sono disattivati;
- non cambia lo stato delle persone;
- non richiede l'apertura del portone;
- non cancella il promemoria reale dell'asciugatrice;
- ripristina il volume precedente del Nest Hub;
- non rimuove un eventuale mute della TV già presente prima del test.

## Utilizzo senza card

Da **Strumenti per sviluppatori → Azioni**:

1. esegui `input_select.select_option` su `input_select.eco_home_scenario_test`;
2. esegui `input_button.press` su `input_button.eco_home_test_vocale`.

Se il Nest Hub è `unavailable`, il test non tenta il TTS e registra l'esito in `input_text.eco_home_ultimo_esito`.

