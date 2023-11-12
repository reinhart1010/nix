---
layout: page
title: common/git-gc (italiano)
description: "Ottimizza il repository locale ripulendolo dai file non necessari."
content_hash: e55ebbb75321f7f25533dfa6e495d76b6f312b19
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-gc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-gc.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-gc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-gc.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-gc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git gc

Ottimizza il repository locale ripulendolo dai file non necessari.
Maggiori informazioni: <https://git-scm.com/docs/git-gc>.

- Ottimizza il repository:

`git gc`

- Ottimizza il repository in modo più aggressivo, impiegando più tempo:

`git gc --aggressive`

- Non eliminare gli oggetti non tracciati (sono eliminati di default):

`git gc --no-prune`

- Non mostrare alcun output:

`git gc --quiet`

- Mostra utilizzo completo:

`git gc --help`
