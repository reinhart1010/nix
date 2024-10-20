---
layout: page
title: common/bedtools (italiano)
description: "Un coltellino svizzero di strumenti per una vasta gamma di operazioni di analisi genomica."
content_hash: 9c78dd0b4c0ec58b0128ee7b9d70d4485e8b3625
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/bedtools.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bedtools.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bedtools

Un coltellino svizzero di strumenti per una vasta gamma di operazioni di analisi genomica.
Usato per intersecare, raggruppare, convertire e contare dati in formato BAM, BED, GFF/GTF, VCF.
Maggiori informazioni: <https://bedtools.readthedocs.io>.

- Interseca il file [a] ed il/i file [b] in base alla sequenza del filamento [s] e salva il risultato in un file specifico:

`bedtools intersect -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_A</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_B1 percorso/del/file_B2 ...</span>` -s > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_output</span>

- Interseca 2 file in base a una [l]eft [o]uter [j]oin ovvero una unione d'insieme di dati ordinati in colonne che restituisce i dati della tabella di sinistra. Es: riporta ogni proprietà presente nel `file1` e NULL dove non c'è sovrapposizione con `file2`:

`bedtools intersect -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file1</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file2</span>` -loj > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_output</span>

- Usa un algoritmo più efficiente per intersecare due file precedentemente ordinati:

`bedtools intersect -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file1</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file2</span>` -sorted > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_output</span>

- Seleziona in un file le prime tre colonne e la quinta [c]olonna utilizzando la sesta colonna per ra[g]gruppare i dati al fine di poter calcolare tramite un'[o]perazione di addizione la somma delle colonne 1,2,3 e 5 per ciascun gruppo:

`bedtools groupby -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>` -c 1-3,5 -g 6 -o sum`

- Converti un file in [i]nput formattato bam in un file formattato bed:

`bedtools bamtobed -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.bam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.bed</span>

- Trova per tutte le proprietà presenti nel `file1.bed` la più vicina nel `file2.bed` e aggiunge la loro [d]istanza in una ulteriore colonna al risultato finale (i file in input devono essere ordinati):

`bedtools closest -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file1.bed</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file2.bed</span>` -d`
