---
layout: page
title: common/git-clean (italiano)
description: "Elimina i file non tracciati dall'albero di lavoro."
content_hash: 23d8624d5a015336cffe2b4509467f41f18b61e2
related_topics:
  - title: English version
    url: /en/common/git-clean.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-clean.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-clean.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-clean.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-clean.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-clean.html
    icon: bi bi-globe
---
# git clean

Elimina i file non tracciati dall'albero di lavoro.
Maggiori informazioni: <https://git-scm.com/docs/git-clean>.

- Elimina i file che non sono tracciati da Git:

`git clean`

- Elimina in modo interattivo i file non tracciati da Git:

`git clean -i`

- Mostra quali file non tracciati sarebbero eliminati, senza però eliminarli davvero:

`git clean --dry-run`

- Forza l'eliminazione dei file non tracciati da Git:

`git clean -f`

- Forza l'eliminazione delle directory non tracciate da Git:

`git clean -fd`

- Elimina i file non tracciati, compresi quelli da ignorare elencati in `.gitignore` e `.git/info/exclude`:

`git clean -x`
