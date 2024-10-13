---
layout: page
title: common/git-clean (italiano)
description: "Elimina i file non tracciati dall'albero di lavoro."
content_hash: 0e1c2f68db5234102358398d8faff795a143e6b9
last_modified_at: 2024-10-13
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
  - title: Indonesia version
    url: /id/common/git-clean.html
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
tldri18n_status: 2
---
# git clean

Elimina i file non tracciati dall'albero di lavoro.
Maggiori informazioni: <https://git-scm.com/docs/git-clean>.

- Elimina i file che non sono tracciati da Git:

`git clean`

- Elimina in modo interattivo i file non tracciati da Git:

`git clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--interactive</span>

- Mostra quali file non tracciati sarebbero eliminati, senza però eliminarli davvero:

`git clean --dry-run`

- Forza l'eliminazione dei file non tracciati da Git:

`git clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--force</span>

- Forza l'eliminazione delle directory non tracciate da Git:

`git clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--force</span>` -d`

- Elimina i file non tracciati, compresi quelli da ignorare elencati in `.gitignore` e `.git/info/exclude`:

`git clean -x`
