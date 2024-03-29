---
layout: page
title: common/git-init (português (Brasil))
description: "Inicializa um novo repositório Git local."
content_hash: ab2e6a4ba3a1ce333d939f461aed50e817002d0f
last_modified_at: 2024-03-14
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
  - title: italiano version
    url: /it/common/git-init.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-init.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git init

Inicializa um novo repositório Git local.
Mais informações: <https://git-scm.com/docs/git-init>.

- Inicializa um novo repositório local:

`git init`

- Inicializa um repositório com o nome especificado para a branch inicial:

`git init --initial-branch=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_branch</span>

- Inicializa um repositório usando SHA256 para os hashes de objeto (requer Git versão 2.29+):

`git init --object-format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sha256</span>

- Inicializa um repositório barebones, adequado para usar como um remoto via SSH:

`git init --bare`
