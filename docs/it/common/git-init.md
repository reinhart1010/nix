---
layout: page
title: common/git-init (italiano)
description: "Inizializza un nuovo repository Git locale."
content_hash: 2dd71d2e71db4a412b6b658d58934fbb875a06be
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-init.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-init.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-init.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-init.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/git-init.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-init.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-init.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git init

Inizializza un nuovo repository Git locale.
Maggiori informazioni: <https://git-scm.com/docs/git-init>.

- Inizializza un nuovo repository locale:

`git init`

- Inizializza un repository con il nome specificato per il ramo iniziale:

`git init --initial-branch=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo</span>

- Inizializza un repository usando SHA256 per gli hash degli oggetti (richiede Git versione 2.29+):

`git init --object-format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sha256</span>

- Inizializza un repository di soli dati, adatto per essere usato come server remoto accessibile via ssh:

`git init --bare`
