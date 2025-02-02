---
layout: page
title: common/tldr-lint (español)
description: "Verifica y formatea páginas `tldr`."
content_hash: 50af55d9d1f45e9abb0bd871c8df91cb0855bfff
last_modified_at: 2024-11-18
related_topics:
  - title: English version
    url: /en/common/tldr-lint.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/tldr-lint.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/tldr-lint.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/tldr-lint.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/tldr-lint.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/tldr-lint.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/tldr-lint.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tldr-lint

Verifica y formatea páginas `tldr`.
Más información: <https://github.com/tldr-pages/tldr-lint>.

- Verifica (lint) todas las páginas:

`tldr-lint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directorio_páginas</span>

- Formatea una página específica hacia `stdout`:

`tldr-lint --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">page.md</span>

- Formatea cada página sin escribir otros archivos o en la salida estándar:

`tldr-lint --format --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directorio_páginas</span>
