---
layout: page
title: common/bup (italiano)
description: "Sistema di backup basato sul formato dei packfile Git, fornendo salvataggi incrementali veloci e deduplicazione globale."
content_hash: d4c7532d6c7dcfba4c05c7e4d8e9ea20ea810747
related_topics:
  - title: English version
    url: /en/common/bup.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bup.html
    icon: bi bi-globe
---
# bup

Sistema di backup basato sul formato dei packfile Git, fornendo salvataggi incrementali veloci e deduplicazione globale.
Maggiori informazioni: <https://github.com/bup/bup>.

- Inizializza una repository di backup nella directory locale specificata:

`bup -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/repository</span>` init`

- Prepara una certa cartella prima di fare un backup:

`bup -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/repository</span>` index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/directory</span>

- Esegui il backup di una cartella in una repository locale:

`bup -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/repository</span>` save -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_backup</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/directory</span>

- Elenca i di backup attualmente nella repository:

`bup -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/repository</span>` ls`

- Ripristina uno specifico backup in una determinata cartella locale:

`bup -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/repository</span>` restore -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/destinazione</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_backup</span>
