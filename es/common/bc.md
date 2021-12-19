---
layout: page
title: common/bc (español)
description: "Un lenguaje de calculadora de precisión arbitraria."
content_hash: a0aeeec794b915d9fe1a8489b3823ea9b12629f5
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
# bc

Un lenguaje de calculadora de precisión arbitraria.
Más información: <https://manned.org/bc>.

- Inicia `bc` en el modo interactivo utilizando la biblioteca matemática estándar:

`bc -l`

- Calcula el resultado de una expresión:

`bc <<< "(1 + 2) * 2 ^ 2"`

- Calcula el resultado de una expresión y fuerza a que el resultado tenga 10 cifras decimales:

`bc <<< "scale=10; 5 / 3"`

- Calcula el resultado de una expresión con el seno y coseno utilizando `mathlib`:

`bc -l <<< "s(1) + c(1)"`
