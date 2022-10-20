---
layout: page
title: common/entr (italiano)
description: "Esegui comandi arbitrari al cambiamento di file."
content_hash: 2133ab9ef8ddf505bee6ba361ee525a9c80edcae
related_topics:
  - title: English version
    url: /en/common/entr.html
    icon: bi bi-globe
---
# entr

Esegui comandi arbitrari al cambiamento di file.
Maggiori informazioni: <https://manned.org/entr>.

- Ricompila con `make` se qualsiasi file in quasiasi sottodirectory cambia:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ag -l</span>` | entr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make</span>

- Ricompila e testa con `make` se qualsiasi file sorgente `.c` nella directory corrente cambia:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls *.c</span>` | entr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'make && make test'</span>

- Invia il segnale `SIGTERM` ad un sottoprocesso ruby precedentemente avviato prima di eseguire `ruby main.rb`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls *.rb</span>` | entr -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby main.rb</span>

- Esegui un comando con il file cambiato (`/_`) come argomento:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls *.sql</span>` | entr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">psql -f</span>` /_`
