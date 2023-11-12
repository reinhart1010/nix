---
layout: page
title: common/autoflake (italiano)
description: "Uno strumento per rimuovere import e variabili inutilizzati da codice Python."
content_hash: e35079061b6f5097d6d61f52f8772d6ea5c6e8ba
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/autoflake.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/autoflake.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/autoflake.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/autoflake.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/autoflake.html
    icon: bi bi-globe
tldri18n_status: 2
---
# autoflake

Uno strumento per rimuovere import e variabili inutilizzati da codice Python.
Maggiori informazioni: <https://github.com/myint/autoflake>.

- Rimuovi le variabili inutilizzate da un file e mostra la differenza:

`autoflake --remove-unused-variables `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.py</span>

- Rimuovi gli import inutilizzati da multipli file mostrando le differenze:

`autoflake --remove-all-unused-imports `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file1.py percorso/del/file2.py ...</span>

- Rimuovi le variabili inutilizzate da un file, sovrascrivendolo:

`autoflake --remove-unused-variables --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.py</span>

- Rimuovi le variabili inutilizzate da tutti i file in una directory, ricorsivamente e sovrascrivendoli:

`autoflake --remove-unused-variables --in-place --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>
