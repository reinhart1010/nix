---
layout: page
title: common/bedtools (italiano)
description: "Un coltellino svizzero di strumenti per analisi genomica."
content_hash: d9a61a1712af9f8aed00d2fc82025141116e2b2f
related_topics:
  - title: English version
    url: /en/common/bedtools.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bedtools.html
    icon: bi bi-globe
---
# bedtools

Un coltellino svizzero di strumenti per analisi genomica.
Usato per intersecare, raggruppare, convertire e contare dati in formato BAM, BED, GFF/GTF, VCF.
Maggiori informazioni: <https://bedtools.readthedocs.io>.

- Interseca i fili genetici delle sequenze contenute in due file diversi e salva il risultato:

`bedtools intersect -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file_1</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file_2</span>` -s > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file_output</span>

- Interseca due file unendo il risultato a sinistra, ovvero riporta ogni feature da `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_1</span>` e NULL dove non c'è sovrapposizione con `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_2</span>`:

`bedtools intersect -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file_1</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file_2</span>` -lof > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file_output</span>

- Usa un algoritmo più efficiente per intersecare due file precedentemente ordinati:

`bedtools intersect -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file_1</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file_2</span>` -sorted > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file_output</span>

- Raggruppa file in base alle prime tre e la quinta colonna e raggruppa la sesta colonna sommandola:

`bedtools groupby -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file</span>` -c 1-3,5 -g 6 -o sum`

- Converti da formato BAM a BED:

`bedtools bamtobed -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file</span>`.bam > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file</span>`.bed`

- Trova per tutte le proprietà in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_1</span>` la più vicina in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_2</span>` e scrivi la loro distanza in una ulteriore colonna (i file in input devono essere ordinati):

`bedtools closest -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file_1</span>`.bed -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file_2</span>`.bed -d`
