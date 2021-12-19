---
layout: page
title: common/bw (italiano)
description: "CLI per accedere e gestire vault Bitwarden."
content_hash: 0f5e4ac4c1994dd80d0fbe820ae2df0b91587bb0
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

- Crea una cartella in un vault bitwarden:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo -n '{"name":"Nome cartella"}' | base64</span>` | bw create folder`
