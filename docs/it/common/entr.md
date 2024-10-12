---
layout: page
title: common/entr (italiano)
description: "Esegui comandi arbitrari al cambiamento di file."
content_hash: 90201cafd140a0628b4613a6b20186ce09b1efb8
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/entr.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/entr.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># entr

Esegui comandi arbitrari al cambiamento di file.
Maggiori informazioni: <https://eradman.com/entrproject/>.

- Ricompila con `make` se qualsiasi file in quasiasi sottodirectory cambia:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ag -l</span>` | entr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make</span>

- Ricompila e testa con `make` se qualsiasi file sorgente `.c` nella directory corrente cambia:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls *.c</span>` | entr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'make && make test'</span>

- Invia il segnale `SIGTERM` ad un sottoprocesso ruby precedentemente avviato prima di eseguire `ruby main.rb`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls *.rb</span>` | entr -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby main.rb</span>

- Esegui un comando con il file cambiato (`/_`) come argomento:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls *.sql</span>` | entr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">psql -f</span>` /_`
