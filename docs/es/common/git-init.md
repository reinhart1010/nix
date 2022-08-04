---
layout: page
title: common/git-init (español)
description: "Inicializa un nuevo repositorio Git local."
content_hash: 3bfbb3fb6966a2560fd30dec5330a731bc495bfb
related_topics:
  - title: Deutsch version
    url: /de/common/git-init.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-init.html
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
---
# git init

Inicializa un nuevo repositorio Git local.
Más información: <https://git-scm.com/docs/git-init>.

- Inicializa un nuevo repositorio local:

`git init`

- Inicializa un repositorio con un nombre especifico para la rama inicial:

`git init --initial-branch=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_rama</span>

- Inicializa un repositorio usando SHA256 como hash del objeto (requiere la versión 2.29+ de Git):

`git init --object-format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sha256</span>

- Inicializa un repositorio vacío, adecuado para usarlo como remoto a través de ssh:

`git init --bare`
