---
layout: page
title: common/expr (español)
description: "Evalúa expresiones y manipula cadenas."
content_hash: 22426ea696337d99ee0c13e5d5d3ea568ba740d5
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/expr.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/expr.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/expr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# expr

Evalúa expresiones y manipula cadenas.
Más información: <https://www.gnu.org/software/coreutils/manual/html_node/expr-invocation.html>.

- Obtiene la longitud de una cadena específica:

`expr length "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena</span>`"`

- Obtiene la subcadena de una cadena con una longitud específica:

`expr substr "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">desde</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">longitud</span>

- Empareja una subcadena específica frente a un patrón:

`expr match "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena</span>`" '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón</span>`'`

- Obtiene la primera posición de un caracter de un conjunto específico en una cadena:

`expr index "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caracteres</span>`"`

- Calcula una expresión matemática específica:

`expr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expresión1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+|-|*|/|%</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expresión2</span>

- Obtiene la primera expresión si su valor no es cero y no nulo, de otro modo, obtiene el segundo:

`expr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expresión1</span>` \| `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expresión2</span>

- Obtiene la primera expresión si ambas expresiones no son cero y no nulas de otro modo obtiene cero:

`expr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expresión1</span>` \& `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expresión2</span>
