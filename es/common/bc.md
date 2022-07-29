---
layout: page
title: common/bc (español)
description: "Un lenguaje de calculadora de precisión arbitraria."
content_hash: ac46108674dcbd516d78f9afc7f26f4542a205bc
related_topics:
  - title: English version
    url: /en/common/bc.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bc.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bc

Un lenguaje de calculadora de precisión arbitraria.
Más información: <https://manned.org/man/bc.1>.

- Inicia `bc` en el modo interactivo utilizando la biblioteca matemática estándar:

`bc -l`

- Calcula el resultado de una expresión:

`bc <<< "(1 + 2) * 2 ^ 2"`

- Calcula el resultado de una expresión y fuerza a que el resultado tenga 10 cifras decimales:

`bc <<< "scale=10; 5 / 3"`

- Calcula el resultado de una expresión con el seno y coseno utilizando `mathlib`:

`bc -l <<< "s(1) + c(1)"`
