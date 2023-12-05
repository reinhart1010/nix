---
layout: page
title: common/git-pr (español)
description: "Comprueba las solicitudes de extracción de cambios (*pull requests*) de GitHub localmente."
content_hash: 6c9b0152516ca70437bed75aa82778766d40b559
last_modified_at: 2023-12-05
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

- Comprueba un pull request específica:

`git pr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_pr</span>

- Comprueba un pull request para un remoto específico:

`git pr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_pr</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remoto</span>

- Comprueba un pull request a partir de su URL:

`git pr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Limpia las ramas antiguas de pull requests:

`git pr clean`
