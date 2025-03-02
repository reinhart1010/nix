---
layout: page
title: common/du (italiano)
description: "Utilizzo del disco: stima e riassumi lo spazio utilizzato da file e directory."
content_hash: b2cdd12b6d9c8fcb1fab311bc3533e6a1551a9f4
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/du.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/du.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/du.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/du.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/du.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/du.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/du.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/du.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/du.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/du.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># du

Utilizzo del disco: stima e riassumi lo spazio utilizzato da file e directory.
Maggiori informazioni: <https://www.gnu.org/software/coreutils/manual/html_node/du-invocation.html>.

- Elenca le dimensioni di una directory ed ogni sotto-directory, nell'unità specificata (B/KiB/MiB):

`du -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">b|k|m</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>

- Elenca le dimensioni di una directory ed ogni sotto-directory, in formato umanamente leggibile (seleziona automaticamente l'unità appropriata per ogni dimensione):

`du -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>

- Mostra la dimensione di una singola directory, in unità umanamente leggibili:

`du -sh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>

- Mostra in formato umanamente leggibile le dimensioni di una directory e tutti i file e directory in essa contenuti:

`du -ah `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>

- Elenca le dimensioni umanamente leggibili di una directory e d ogni sotto-directory, fino ad N livelli di profondità:

`du -h --max-depth=N `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>

- Mostra le dimensioni umanamente leggibili di tutti i file `.jpg` nelle sottodirectory della directory corrente, e mostra il totale cumulativo alla fine:

`du -ch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*/*.jpg</span>
