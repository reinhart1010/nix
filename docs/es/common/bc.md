---
layout: page
title: common/bc (español)
description: "Un lenguaje de calculadora de precisión arbitraria."
content_hash: c44d6423893256560729bf0fe0d0991490d4edad
last_modified_at: 2024-01-07
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
  - title: português (Brasil) version
    url: /pt_BR/common/bc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/bc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bc

Un lenguaje de calculadora de precisión arbitraria.
Vea también: `dc`.
Más información: <https://manned.org/man/bc.1>.

- Inicia una sesión interactiva:

`bc`

- Inicia una sesión interactiva con la biblioteca matemática estándar activada:

`bc --mathlib`

- Calcula una expresión:

`echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5 / 3</span>`' | bc`

- Ejecuta un script:

`bc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/script.bc</span>

- Calcula una expresión con la escala especificada:

`echo 'scale = `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>`; `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5 / 3</span>`' | bc`

- Calcula una función seno/coseno/arctangente/logaritmo natural/exponencial utilizando `mathlib`:

`echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s|c|a|l|e</span>`(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>`)' | bc --mathlib`
