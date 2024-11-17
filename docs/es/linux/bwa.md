---
layout: page
title: linux/bwa (español)
description: "Herramienta de alineación Burrows-Wheeler."
content_hash: 77514dd8d49553d0bc39cfc32cdb51705ba18b95
last_modified_at: 2024-11-17
related_topics:
  - title: English version
    url: /en/linux/bwa.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/bwa.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bwa

Herramienta de alineación Burrows-Wheeler.
Mapeador de secuencias de ADN cortas y poco divergentes frente a un gran genoma de referencia, como el genoma humano.
Más información: <https://github.com/lh3/bwa>.

- Indexa el genoma de referencia:

`bwa index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/referencia.fa</span>

- Mapea las lecturas de un solo extremo (secuencias) al genoma indexado utilizando 32 subprocesos y comprime el resultado para ahorrar espacio:

`bwa mem -t 32 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/referencia.fa</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/lectura_solo_extremo.fq.gz</span>` | gzip > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/alineamiento_solo_extremo.sam.gz</span>

- Mapea las lecturas del par final (secuencias) al genoma indexado usando 32 subprocesos y comprime el resultado para ahorrar espacio:

`bwa mem -t 32 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/referencia.fa</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/lectura_par_final_1.fq.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/lectura_par_final_2.fq.gz</span>` | gzip > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/alineamiento_par_final.sam.gz</span>

- Mapea las lecturas del par final (secuencias) al genoma indexado usando 32 subprocesos con [M]arcadores divididos más cortos como secundarios para la compatibilidad del archivo SAM de salida con el software Picard y luego comprime el resultado:

`bwa mem -M -t 32 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/referencia.fa</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/lectura_par_final_1.fq.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/lectura_par_final_2.fq.gz</span>` | gzip > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/alineamiento_par_final.sam.gz</span>

- Mapea las lecturas finales del par (secuencias) al genoma indexado usando 32 subprocesos con [C]omentarios FASTA/Q (p. ej. BC:Z:CGTAC) anexando a un resultado comprimido:

`bwa mem -C -t 32 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/referencia.fa</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/lectura_par_final_1.fq.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/lectura_par_final_2.fq.gz</span>` | gzip > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/lectura_par_final.sam.gz</span>
