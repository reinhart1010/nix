---
layout: page
title: common/bup (italiano)
description: "Sistema di backup basato sul formato dei packfile Git, fornendo salvataggi incrementali veloci e deduplicazione globale."
content_hash: 24577a5b9bf8447d0f407fad25a2600edd9766bf
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/bup.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bup.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/bup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bup

Sistema di backup basato sul formato dei packfile Git, fornendo salvataggi incrementali veloci e deduplicazione globale.
Maggiori informazioni: <https://github.com/bup/bup>.

- Inizializza una repository di backup nella directory locale specificata:

`bup -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/repository</span>` init`

- Prepara una certa directory prima di fare un backup:

`bup -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/repository</span>` index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>

- Esegui il backup di una directory in una repository locale:

`bup -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/repository</span>` save -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_backup</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>

- Elenca i di backup attualmente nella repository:

`bup -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/repository</span>` ls`

- Ripristina uno specifico backup in una determinata directory locale:

`bup -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/repository</span>` restore -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/destinazione</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_backup</span>
