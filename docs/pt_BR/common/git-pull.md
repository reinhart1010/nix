---
layout: page
title: common/git-pull (português (Brasil))
description: "Obtém branch de um repositório remoto e mescla-a ao repositório local."
content_hash: 0d0c6a718c65f622bbd869d62473969686720835
last_modified_at: 2023-10-15
related_topics:
  - title: Deutsch version
    url: /de/common/git-pull.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-pull.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-pull.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-pull.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-pull.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-pull.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-pull.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-pull.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-pull.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git pull

Obtém branch de um repositório remoto e mescla-a ao repositório local.
Mais informações: <https://git-scm.com/docs/git-pull>.

- Baixa as alterações do repositório remoto padrão e mescla-as:

`git pull`

- Baixa as alterações do repositório remoto padrão e usa o avanço rápido:

`git pull --rebase`

- Baixa as alterações de um determinado repositório remoto e branch, então, mescla-as no HEAD:

`git pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_remoto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch</span>
