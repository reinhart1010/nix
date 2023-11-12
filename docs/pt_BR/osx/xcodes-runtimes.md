---
layout: page
title: osx/xcodes-runtimes (português (Brasil))
description: "Gerencia runtimes do Simulador Xcode."
content_hash: 19acccf45363eb49a67b44eb50ee997d6f65920f
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/xcodes-runtimes.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/xcodes-runtimes.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/xcodes-runtimes.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># xcodes runtimes

Gerencia runtimes do Simulador Xcode.
Mais informações: <https://github.com/xcodesorg/xcodes>.

- Lista todos os runtimes do Simulador disponíveis:

`xcodes runtimes --include-betas`

- Baixa um runtime do Simulador:

`xcodes runtimes download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome-do-runtime</span>

- Baixa e instala um runtime do Simulador:

`xcodes runtimes install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome-do-runtime</span>
