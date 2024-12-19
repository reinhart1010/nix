---
layout: page
title: common/expr (español)
description: "Evalúa expresiones y manipula cadenas."
content_hash: b952fea6bef7d71aee7aeda5cee49fd1d552d92b
last_modified_at: 2024-12-19
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
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/expr.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># expr

Evalúa expresiones y manipula cadenas.
Más información: <https://www.gnu.org/software/coreutils/expr>.

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
