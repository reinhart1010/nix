---
layout: page
title: common/autoflake (italiano)
description: "Uno strumento per rimuovere import e variabili inutilizzati da codice Python."
content_hash: 53f1d0dfe358cb96e137aeaac31a4627dc616f1b
related_topics:
  - title: English version
    url: /en/common/autoflake.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/autoflake.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/autoflake.html
    icon: bi bi-globe
---
# autoflake

Uno strumento per rimuovere import e variabili inutilizzati da codice Python.
Maggiori informazioni: <https://github.com/myint/autoflake>.

- Rimuovi le variabili inutilizzate da un file e mostra la differenza:

`autoflake --remove-unused-variables `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.py</span>

- Rimuovi gli import inutilizzati da multipli file mostrando le differenze:

`autoflake --remove-all-unused-imports `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1.py</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2.py</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file3.py</span>

- Rimuovi le variabili inutilizzate da un file, sovrascrivendolo:

`autoflake --remove-unused-variables --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.py</span>

- Rimuovi le variabili inutilizzate da tutti i file in una cartella, ricorsivamente e sovrascrivendoli:

`autoflake --remove-unused-variables --in-place --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/cartella</span>
