---
layout: page
title: osx/bc (español)
description: "Un lenguaje de calculadora de precisión arbitraria."
content_hash: 976861917deff7ac18e3ec839407d318a740dd63
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/bc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/bc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bc

Un lenguaje de calculadora de precisión arbitraria.
Ver también: `dc`.
Más información: <https://manned.org/man/freebsd-13.0/bc.1>.

- Inicia una sesión interactiva:

`bc`

- Inicia una sesión interactiva con la biblioteca mathlib estándar activada:

`bc --mathlib`

- Calcula una expresión:

`bc --expression='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5 / 3</span>`'`

- Ejecuta un script:

`bc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/script.bc</span>

- Calcula una expresión con la escala especificada:

`bc --expression='scale = `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>`; `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5 / 3</span>`'`

- Calcula una función seno/coseno/arctangente/logaritmo natural/exponencial utilizando `mathlib`:

`bc --mathlib --expression='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s|c|a|l|e</span>`(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>`)'`
