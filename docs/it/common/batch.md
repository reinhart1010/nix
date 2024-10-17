---
layout: page
title: common/batch (italiano)
description: "Esegui comandi nel futuro quando il carico di lavoro del sistema lo permette."
content_hash: f872f58a6176ff49d9df5cefaf1e2f6b51383616
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/batch.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/batch.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/batch.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/batch.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># batch

Esegui comandi nel futuro quando il carico di lavoro del sistema lo permette.
Il servizio atd (o atrun) deve essere attivo per eseguire i comandi.
Maggiori informazioni: <https://manned.org/batch>.

- Esegui i comandi inseriti standard input (premere `Ctrl + D` dopo aver inserito i comandi):

`batch`

- Esegui un comando da standard input:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./mio_script.sh</span>`" | batch`

- Esegui comandi contenuti in un dato file:

`batch -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>
