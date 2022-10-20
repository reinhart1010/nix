---
layout: page
title: common/bw (italiano)
description: "CLI per accedere e gestire vault Bitwarden."
content_hash: 79332b81fe4691d05c9e077ded802ccb33e4a0c6
related_topics:
  - title: English version
    url: /en/common/bw.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bw.html
    icon: bi bi-globe
---
# bw

CLI per accedere e gestire vault Bitwarden.
Maggiori informazioni: <https://help.bitwarden.com/article/cli/>.

- Esegui il login ad un account Bitwarden:

`bw login`

- Esegui il logout da un account Bitwarden:

`bw logout`

- Cerca e mostra oggetti in un vault Bitwarden:

`bw list items --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">github</span>

- Mostra un particolare oggetto contenuto in un vault Bitwarden:

`bw get item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">github</span>

- Crea una directory in un vault bitwarden:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo -n '{"name":"Nome directory"}' | base64</span>` | bw create folder`
