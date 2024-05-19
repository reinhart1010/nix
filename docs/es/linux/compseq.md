---
layout: page
title: linux/compseq (español)
description: "Calcula la composición de palabras únicas en secuencias."
content_hash: 673b352895f17e1b508016d4bfe2d0cbc0173b44
last_modified_at: 2024-05-19
related_topics:
  - title: English version
    url: /en/linux/compseq.html
    icon: bi bi-globe
tldri18n_status: 2
---
# compseq

Calcula la composición de palabras únicas en secuencias.
Más información: <https://www.bioinformatics.nl/cgi-bin/emboss/help/compseq/>.

- Cuenta frecuencias observadas de palabras en un archivo FASTA, proporcionando valores de parámetros interactivamente:

`compseq `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.fasta</span>

- Cuenta frecuencias observadas de pares de aminoácidos en un archivo FASTA, y guarda el resultado en un archivo de texto:

`compseq `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_proteina.fasta</span>` -word 2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_salida.comp</span>

- Cuenta las frecuencias observadas de hexanucleótidos en un archivo FASTA, luego guarda el resultado en un archivo de texto e ignora los recuentos cero:

`compseq `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_entrada.fasta</span>` -word 6 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_salida.comp</span>` -nozero`

- Cuenta las frecuencias observadas de codones en un marco de lectura concreto, ignorando cualquier recuento superpuesto (es decir, desplaza la ventana en longitud de palabra 3):

`compseq -sequence `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_ingreso_rna.fasta</span>` -word 3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_salida.comp</span>` -nozero -frame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Cuenta las frecuencias observadas de codones desplazados en 3 posiciones; ignorando los recuentos superpuestos (debería informar de todos los codones excepto el primero):

`compseq -sequence `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_ingreso_rna.fasta</span>` -word 3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_salida.comp</span>` -nozero -frame 3`

- Cuenta tripletes de aminoácidos en un archivo FASTA y compara con una ejecución anterior de `compseq` para calcular los valores de frecuencia esperados y normalizados:

`compseq -sequence `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/proteoma_humano.fasta</span>` -word 3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_salida1.comp</span>` -nozero -infile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_salida2.comp</span>

- Aproxima el comando anterior sin un archivo previamente preparado, calculando las frecuencias esperadas usando las frecuencias de una sola base/residuo en la(s) secuencia(s) de entrada suministrada(s):

`compseq -sequence `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/proteoma_humano.fasta</span>` -word 3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_salida.comp</span>` -nozero -calcfreq`

- Muestra ayuda (utiliza `-help -verbose` para obtener más información sobre los calificadores asociados y generales):

`compseq -help`
