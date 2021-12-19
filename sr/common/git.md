---
layout: page
title: common/git (српски)
description: "Distribuirani sistem kontrole verzija."
content_hash: 844c9f7939655575da4010ccf4a7229b208cb990
related_topics:
  - title: Deutsch version
    url: /de/common/git.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/git.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git.html
    icon: bi bi-globe
---
# git

Distribuirani sistem kontrole verzija.
Neke podkomande kao što je `git commit` imaju svoj primer u dokumentaciji.
Više informacija na: <https://git-scm.com/>.

- Proverava Git verziju:

`git --version`

- Prikazuje opštu pomoć:

`git --help`

- Prikazuje pomoć o Git podkomandi (npr. `commit`, `log`, itd.):

`git help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">podkomanda</span>

- Izvršava Git podkomandu:

`git `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">podkomanda</span>

- Izvršava Git podkomandu u zadatoj početnoj lokaciji repozitorijuma:

`git -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">putanja/do/repozitorijuma</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">podkomanda</span>

- Izvršava Git podkomandu sa zadatim setom konfiguracija:

`git -c '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">config.key</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">podkomanda</span>
