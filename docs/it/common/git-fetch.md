---
layout: page
title: common/git-fetch (italiano)
description: "Scarica oggetti e riferimenti da un repository remoto."
content_hash: eaac816d048a05bb856458b8c445f6d0f7a33772
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-fetch.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-fetch.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-fetch.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-fetch.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-fetch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git fetch

Scarica oggetti e riferimenti da un repository remoto.
Maggiori informazioni: <https://git-scm.com/docs/git-fetch>.

- Scarica le ultime modifiche dal repository remoto di origine (upstream) di default, se definito:

`git fetch`

- Scarica i nuovi rami da un dato repository remoto di origine:

`git fetch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_repository_remoto</span>

- Scarica le ultime modifiche da tutti i repository remoti di origine:

`git fetch --all`

- Scarica anche i tag dal repository remoto di origine:

`git fetch --tags`

- Elimina i riferimenti locali ai rami remoti che sono stati eliminati dal repositoy di origine:

`git fetch --prune`
