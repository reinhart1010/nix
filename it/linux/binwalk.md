---
layout: page
title: linux/binwalk (italiano)
description: "Strumento per l'analisi di file binari."
content_hash: 1feda0952eaa5c5a16d77c020bb9c03fd89f1944
related_topics:
  - title: English version
    url: /en/linux/binwalk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/binwalk.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/binwalk.html
    icon: bi bi-globe
---
# binwalk

Strumento per l'analisi di file binari.
Maggiori informazioni: <https://github.com/ReFirmLabs/binwalk>.

- Scansiona un file binario:

`binwalk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/file</span>

- Estrae file da un binario, specificando la cartella di output:

`binwalk --extract --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cartella_di_output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/file</span>

- Estrae file in maniera ricorsiva a partire da un binario, limitando la profondità di ricorsione a 2 livelli:

`binwalk --extract --matryoshka --depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/file</span>

- Estrae file da un binario utilizzando una particolare firma (ad esempio il MIME Type):

`binwalk --dd '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">png image:png</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/file</span>

- Analizza l'entropia di un binario e salva il grafico con lo stesso filename del binario, con l'estensione `.png` in fondo:

`binwalk --entropy --save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/file</span>

- Combina analisi di entropia, firme e opcode in un unico comando:

`binwalk --entropy --signature --opcodes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/file</span>
