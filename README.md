# Buy Inefficiency

**English abstract.** Buy Inefficiency is a public, versioned specification for an index of *computational efficiency*: how much energy is required, over time, to correctly complete a fixed basket of computational workloads. The method of computation is not prescribed. An optional later phase may design an asset for economic exposure to that index; the index and any token are distinct objects.

---

## Cos’è

Buy Inefficiency misura il progresso informatico come **capacità di ottenere gli stessi risultati con meno risorse fisiche** — in particolare meno energia — senza dipendere da una tecnologia, un’azienda o un’architettura specifica.

Il sistema si basa su un **paniere pubblico di lavori computazionali**. Per ciascun lavoro sono definiti input, risultato richiesto e condizioni di verifica. Non si impone *come* produrre il risultato. Conta l’energia necessaria a produrlo correttamente.

Quando nuove tecniche (hardware, algoritmi, memorie, compilatori, paradigmi di calcolo, o innovazioni oggi imprevedibili) riducono l’energia per lo stesso paniere, l’indice registra un aumento di efficienza. L’indice **non sceglie un vincitore tecnologico**: misura il risultato del progresso, qualunque ne sia l’origine.

## Cosa non è (ancora)

- **Non è un token.** La specifica dell’indice definisce *cosa* si misura. Non garantisce, da sola, che un asset ne segua economicamente il valore.
- **Non è una misura universale definitiva.** È una specifica pubblica e versionata. Una comunità può adottarla o crearne una derivata (fork). Ogni fork è un nuovo indice e non altera retroattivamente la serie storica dell’originale.
- **Non è un ranking di aziende o di chip.** Non premia un produttore: premia il risultato energetico sul paniere.

## Stato del progetto

| Elemento | Stato |
|----------|--------|
| Idea e principio economico | Documentati |
| [Index Spec v0.1](./INDEX_SPEC_v0.1.md) | Bozza pubblica |
| [Pitch](./PITCH.md) | Bozza pubblica |
| Paniere concreto di workload | TBD |
| Protocollo di laboratorio / misura energetica | Strutturato, dettagli TBD |
| Asset / token di esposizione | **Non iniziato** (fase separata) |

## Principio economico

*Buy Inefficiency* = acquistare esposizione al divario tra ciò che il computing riesce a fare oggi e ciò che potrà fare, in futuro, con le stesse risorse fisiche.

L’ipotesi non riguarda una particolare azienda, criptovaluta o tecnologia: riguarda la capacità generale di migliorare il rapporto tra risorse consumate e lavoro computazionale prodotto.

## Documenti

- [`INDEX_SPEC_v0.1.md`](./INDEX_SPEC_v0.1.md) — specifica formale dell’indice
- [`PITCH.md`](./PITCH.md) — testo breve da condividere
- [`CONTRIBUTING.md`](./CONTRIBUTING.md) — come proporre workload, fork, issue

## Licenza

Contenuti di questo repository: [CC BY 4.0](./LICENSE).

## Autore

Gio Mario Lasagna — bozza iniziale, settembre 2026.
