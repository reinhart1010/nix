---
layout: page
title: common/git-pr (español)
description: "Comprueba las solicitudes de extracción de cambios (*pull requests*) de GitHub localmente."
content_hash: 7fa41b23ae0b309049875df41c8c7f122cdbda0f
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-pr.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-pr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-pr.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-pr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git pr

Comprueba las solicitudes de extracción de cambios (*pull requests*) de GitHub localmente.
Más información: <https://github.com/tj/git-extras/blob/master/Commands.md#git-pr>.

- Comprueba una pull request específica:

`git pr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_pr</span>

- Comprueba una pull request para un remoto específico:

`git pr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_pr</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remoto</span>

- Comprueba una pull request a partir de su URL:

`git pr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Limpia las ramas antiguas de pull requests:

`git pr clean`
