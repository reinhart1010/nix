---
layout: page
title: common/git-rev-parse (italiano)
description: "Mostra i metadati relativi a specifiche revisioni."
content_hash: 3a3b06b6478ec837700878fc3ea9e4b25eaa80af
last_modified_at: 2023-11-12
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
  - title: Türkçe version
    url: /tr/common/git-rev-parse.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git rev-parse

Mostra i metadati relativi a specifiche revisioni.
Maggiori informazioni: <https://git-scm.com/docs/git-rev-parse>.

- Mostra l'hash del commit di un ramo:

`git rev-parse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo</span>

- Mostra il nome del ramo corrente:

`git rev-parse --abbrev-ref `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Mostra il percorso assoluto della directory di root:

`git rev-parse --show-toplevel`
