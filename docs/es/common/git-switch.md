---
layout: page
title: common/git-switch (español)
description: "Alterna entre ramas Git. Requiere una versión 2.23+ de Git."
content_hash: 6dcd430d33638dedfc55ecd44969d37d15ad677d
related_topics:
  - title: Deutsch version
    url: /de/common/git-switch.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-switch.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-switch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-switch.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-switch.html
    icon: bi bi-globe
---
# git switch

Alterna entre ramas Git. Requiere una versión 2.23+ de Git.
Véase también `git checkout`.
Más información: <https://git-scm.com/docs/git-switch>.

- Cambia a una rama existente:

`git switch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_rama</span>

- Crea una nueva rama y se cambia a esta:

`git switch --create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_rama</span>

- Crea una nueva rama basada en un commit específico y se cambia a esta:

`git switch --create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_rama</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Cambia a la rama anterior:

`git switch -`

- Cambia a una rama y actualiza todos los submódulos para coincidir:

`git switch --recurse-submodules `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_rama</span>

- Cambia a una rama y automáticamente fusiona la rama actual y cualquier cambio sin commit en ella:

`git switch --merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_rama</span>
