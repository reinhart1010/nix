---
layout: page
title: common/act (português (Brasil))
description: "Executa GitHub Actions localmente utilizando Docker."
content_hash: 8c6d7bbfb47a03ac5740aaf162dacd0a25022115
last_modified_at: 2024-10-28
related_topics:
  - title: English version
    url: /en/common/act.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/act.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/act.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/act.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/act.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/act.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/act.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/act.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># act

Executa GitHub Actions localmente utilizando Docker.
Mais informações: <https://github.com/nektos/act>.

- Lista ações disponíveis:

`act -l`

- Executa evento padrão:

`act`

- Executa evento específico:

`act `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tipo_de_evento</span>

- Executa um job específico:

`act -j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>

- Não executa realmente as ações (ex.: um dry run):

`act -n`

- Mostra verbose logs:

`act -v`

- Executa um workflow específico com o evento de push:

`act push -W `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/workflow</span>
