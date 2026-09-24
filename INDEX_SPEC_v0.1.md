# Buy Inefficiency — Index Specification v0.1

**Status:** Draft  
**Version:** 0.1  
**Date:** 2026-09-24  
**License:** CC BY 4.0  

**English abstract.** This document defines a public, versioned specification for an index of computational efficiency: the evolution of energy required to correctly complete a fixed basket of computational workloads, without prescribing the computational method. Forks create new indices and do not rewrite the original history. This specification does not define a token or any economic exposure mechanism.

---

## 1. Purpose

Definire una specifica pubblica e versionata che permetta di:

1. Dichiarare un **paniere** di lavori computazionali confrontabili.
2. Misurare l’**energia** necessaria a completarli correttamente.
3. Costruire una **serie temporale** dell’efficienza sul paniere, indipendente dalla tecnologia usata.
4. Consentire **adozione** e **fork** senza autorità centrale.

Il progresso informatico, in questa specifica, non è solo aumento della potenza disponibile, ma anche riduzione delle risorse fisiche (in particolare energia) necessarie a ottenere gli stessi risultati verificabili.

## 2. Scope and non-goals

### In scope

- Definizione di workload, paniere, verifica, confini di misura energetica.
- Regole di versioning e di fork.
- Requisiti di trasparenza e riproducibilità.

### Non-goals (v0.1)

- Non definire un token, una tokenomics, un oracle on-chain, o un meccanismo di esposizione economica.
- Non dichiarare una misura universale e definitiva dell’efficienza computazionale.
- Non produrre ranking di aziende, prodotti o architetture come obiettivo primario.
- Non fissare in v0.1 l’elenco concreto dei workload (TBD) né i dettagli di laboratorio (TBD).

## 3. Definitions

| Termine | Definizione |
|---------|-------------|
| **Workload** | Un lavoro computazionale con input, risultato richiesto e condizioni di verifica specificati. Il metodo di soluzione non è prescritto. |
| **Basket (paniere)** | Insieme versionato di workload che costituisce l’unità di misura dell’indice. |
| **Verification** | Procedura che decide se un risultato è corretto rispetto alla specifica del workload. |
| **Energy measurement boundary** | Confine fisico/logico entro cui si contabilizza l’energia associata all’esecuzione del paniere (TBD in dettaglio operativo). |
| **Run** | Tentativo di completare (parte di) un paniere su un dato sistema, con log di energia e di verifica. |
| **Efficiency observation** | Energia misurata (entro i confini dichiarati) per completare correttamente il paniere, o una sua parte dichiarata, in un run valido. |
| **Index series** | Sequenza temporale di osservazioni (o aggregati) pubblicate per una specifica versione di paniere + protocollo. |
| **Fork** | Nuova specifica derivata (paniere e/o protocollo modificati) che costituisce un **nuovo** indice, con propria serie storica. |

## 4. Basket requirements

Un paniere conforme a questa specifica deve:

1. Essere **pubblico** (testo e artefatti necessari disponibili).
2. Elencare ciascun workload con:
   - identificatore stabile;
   - descrizione;
   - input (o generatore di input) deterministico o campionato con semi dichiarati;
   - formato e criterio del risultato richiesto;
   - procedura di verifica;
   - eventuali vincoli ambientali (TBD: temperatura, precisione numerica, ecc.).
3. **Non** prescrivere l’algoritmo, l’hardware, o il paradigma di calcolo.
4. Dichiarare se i workload sono aperti (input pubblici) o a “sfida” (input rivelati al momento della misura) — policy TBD per v0.1+.
5. Essere identificato da una **versione** (es. `basket-0.1.0`).

### Basket v0.1 — contenuti

**TBD.** L’elenco dei workload concreti non è ancora fissato. Verrà aggiunto in una revisione minore o in v0.2 senza rompere le regole di questa specifica strutturale, oppure tramite documento `BASKET_vX.md` collegato.

## 5. Measurement protocol

### 5.1 Principio

Ciò che conta per l’osservazione primaria è la **quantità di energia** necessaria a produrre **correttamente** i risultati del paniere, entro i confini di misura dichiarati.

Non sono metriche primarie (da sole) di questa specifica:

- numero di operazioni;
- tipo di processore;
- solo il tempo di wall-clock (può essere riportato come metadato).

### 5.2 Passi di un run valido

1. Dichiarare la **versione** di paniere e di protocollo.
2. Dichiarare il **sistema sotto test** (descrizione libera: hardware, software, configurazione rilevante).
3. Eseguire i workload **senza** violare i vincoli del paniere.
4. Applicare la **verifica** a ogni workload richiesto.
5. Registrare l’**energia** entro il measurement boundary dichiarato.
6. Pubblicare i log necessari alla riproduzione o all’audit (formato TBD).

Un run è **invalido** se la verifica fallisce su un workload obbligatorio, se i confini energetici non sono dichiarati, o se i log richiesti dalla versione del protocollo mancano.

### 5.3 Energy accounting (struttura; dettagli TBD)

Per ogni run valido si deve dichiarare almeno:

- unità energetica (raccomandato: joule / watt-ora — **TBD conferma**);
- confini (es. solo package CPU/GPU, intera macchina, rack — **TBD**);
- strumento o metodo di misura (powermeter, RAPL, PDU, stima modellata — **TBD**; le stime modellate vanno etichettate come tali);
- intervallo temporale allineato all’esecuzione del paniere;
- eventuali correzioni (idle subtraction, ecc. — **TBD policy**).

### 5.4 Aggregazione dell’indice (bozza)

**TBD.** Possibili direzioni (non normative in v0.1):

- energia totale del paniere nel tempo;
- media ponderata su workload;
- indice normalizzato a una baseline dichiarata (es. prima osservazione pubblica = 100).

La formula ufficiale sarà fissata quando esiste almeno un paniere concreto e una baseline riproducibile.

## 6. Versioning and forks

### 6.1 Versioning

Questa specifica usa versioni semantiche a livello di documento (`v0.1`, `v0.2`, …).

- Cambiamenti che alterano il significato delle osservazioni storiche richiedono una **nuova versione maggiore** del paniere/protocollo e, di fatto, una nuova serie.
- Clarifications senza impatto sulle serie possono essere patch/documentazione.

### 6.2 Forks

Chiunque può pubblicare una specifica derivata (nuovo paniere, nuovi criteri, diverso ambito).

Regole:

1. Un fork **deve** dichiarare la specifica di origine e le differenze.
2. Un fork costituisce un **nuovo indice** con **nuova** serie storica.
3. Un fork **non** altera retroattivamente la serie dell’indice originale.
4. La legittimità deriva da trasparenza, riproducibilità e adozione — non da un’autorità centrale.

## 7. Reproducibility

Per quanto praticabile, ogni osservazione pubblicata dovrebbe consentire a terzi di:

- comprendere cosa è stato eseguito;
- ripetere o auditare la verifica;
- valutare i confini energetici.

Formati di log, hashing degli artefatti e checklist di audit: **TBD**.

## 8. Governance / adoption (lightweight)

Non esiste un’autorità che dichiari “questa è *la* efficienza computazionale”.

- L’adozione di una specifica o di un paniere è volontaria.
- Il coordinamento può avvenire via issue/PR su repository pubblici.
- Conflitti di definizione si risolvono preferibilmente con **fork** chiari piuttosto che con riscritture silenziose della storia.

## 9. Relationship to any future asset

L’indice e un eventuale asset finanziario/crypto sono **oggetti distinti**.

Questa specifica:

- **non** crea un token;
- **non** implica che un token esista o debba esistere;
- **non** garantisce che un asset segua il valore dell’indice.

Qualsiasi meccanismo di esposizione economica è una **fase separata** del progetto e richiederà un documento dedicato.

## 10. Changelog

### v0.1 — 2026-09-24

- Prima bozza pubblica della struttura: definizioni, requisiti di paniere, protocollo (con TBD), versioning/fork, riproducibilità, governance leggera.
- Nessun paniere concreto; nessuna formula d’indice normativa; nessun asset.

## 11. Open questions / future work

1. Quali workload entrano nel primo paniere pubblico?
2. Quali confini energetici sono abbastanza rigorosi e abbastanza praticabili?
3. Come gestire input “sfida” vs input aperti?
4. Come normalizzare osservazioni tra laboratori diversi?
5. Quale formula d’indice adottare dopo la baseline?
6. Se e come (fase successiva) un asset possa dare esposizione all’indice senza confondere i due oggetti.

---

Fine della specifica v0.1.
