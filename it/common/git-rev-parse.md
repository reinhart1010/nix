---
layout: page
title: common/git-rev-parse (italiano)
description: "Mostra i metadati relativi a specifiche revisioni."
content_hash: 6d0156c5b10b382491c7397d9f7463e51c0b0c3b
related_topics:
  - title: English version
    url: /en/common/git-rev-parse.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-rev-parse.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-rev-parse.html
    icon: bi bi-globe
---
# git rev-parse

Mostra i metadati relativi a specifiche revisioni.
Maggiori informazioni: <https://git-scm.com/docs/git-rev-parse>.

- Mostra l'hash del commit di un ramo:

`git rev-parse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo</span>

- Mostra il nome del ramo corrente:

`git rev-parse --abbrev-ref `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Mostra il percorso assoluto della cartella di root:

`git rev-parse --show-toplevel`
