---
layout: page
title: common/git-clone (italiano)
description: "Clona un repository esistente."
content_hash: 0fc21b56e79bf84cb422cefc44b15b8c2cc8ce1c
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-clone.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-clone.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-clone.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-clone.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-clone.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-clone.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-clone.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-clone.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-clone.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-clone.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-clone.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git clone

Clona un repository esistente.
Maggiori informazioni: <https://git-scm.com/docs/git-clone>.

- Clona un repository remoto esistente:

`git clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_repository_remoto</span>

- Clona un repository remoto insieme ai suoi sottomoduli:

`git clone --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_repository_remoto</span>

- Clona un repository locale:

`git clone -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/repository/locale</span>

- Clona in modalità silenziosa:

`git clone -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_repository_remoto</span>

- Clona un repository remoto scaricando solo i 10 commit più recenti del ramo principale (utile per risparmiare tempo):

`git clone --depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_repository_remoto</span>
