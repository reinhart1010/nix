---
layout: page
title: common/act (português (Brasil))
description: "Executa GitHub Actions localmente utilizando Docker."
content_hash: 6a2d824451ad91a24b89b953aa3d5189ac2a88ad
last_modified_at: 2023-11-12
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

- Lista acoes disponiveis:

`act -l`

- Executa evento padrão:

`act`

- Executa evento especifico:

`act `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tipo_de_evento</span>

- Executa acao especifica:

`act -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">acao_id</span>

- Nao executa realmente as acoes (i.e. um dry run):

`act -n`

- Mostra verbose logs:

`act -v`
