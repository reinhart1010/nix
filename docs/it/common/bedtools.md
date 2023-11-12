---
layout: page
title: common/bedtools (italiano)
description: "Un coltellino svizzero di strumenti per analisi genomica."
content_hash: 0c53fc40442298e302158b9ae38dc92a6b736b35
last_modified_at: 2023-11-12
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

Un coltellino svizzero di strumenti per analisi genomica.
Usato per intersecare, raggruppare, convertire e contare dati in formato BAM, BED, GFF/GTF, VCF.
Maggiori informazioni: <https://bedtools.readthedocs.io>.

- Interseca i fili genetici delle sequenze contenute in due file diversi e salva il risultato:

`bedtools intersect -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file1</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file2</span>` -s > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_output</span>

- Interseca due file unendo il risultato a sinistra, ovvero riporta ogni feature da `file1` e NULL dove non c'è sovrapposizione con `file2`:

`bedtools intersect -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file1</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file2</span>` -lof > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_output</span>

- Usa un algoritmo più efficiente per intersecare due file precedentemente ordinati:

`bedtools intersect -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file1</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file2</span>` -sorted > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_output</span>

- Raggruppa file in base alle prime tre e la quinta colonna e raggruppa la sesta colonna sommandola:

`bedtools groupby -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>` -c 1-3,5 -g 6 -o sum`

- Converti da formato BAM a BED:

`bedtools bamtobed -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.bam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.bed</span>

- Trova per tutte le proprietà in `file1` la più vicina in `file2` e scrivi la loro distanza in una ulteriore colonna (i file in input devono essere ordinati):

`bedtools closest -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file1.bed</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file2.bed</span>` -d`
