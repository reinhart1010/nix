---
layout: page
title: common/bc (español)
description: "Un lenguaje de calculadora de precisión arbitraria."
content_hash: 161378e65464b45804a7f981573f512addada950
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/bc.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/bc.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bc.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/bc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/bc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bc

Un lenguaje de calculadora de precisión arbitraria.
Ver también: `dc`.
Más información: <https://manned.org/man/bc.1>.

- Inicia una sesión interactiva:

`bc`

- Inicia una sesión interactiva con la biblioteca matemática estándar activada:

`bc --mathlib`

- Calcula una expresión:

`echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5 / 3</span>`'' | bc`

- Ejecuta un script:

`bc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/script.bc</span>

- Calcula una expresión con la escala especificada:

`echo 'scale = `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>`; `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5 / 3</span>`'' | bc`

- Calcula una función seno/coseno/arctangente/logaritmo natural/exponencial utilizando `mathlib`:

`echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s|c|a|l|e</span>`(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>`)'' | bc --mathlib`
