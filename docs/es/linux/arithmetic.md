---
layout: page
title: linux/arithmetic (español)
description: "Examen de problemas simples de aritmética."
content_hash: 06e53495f0830b9becf0a6079e203da8a31cf26e
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/linux/arithmetic.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/arithmetic.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/arithmetic.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/arithmetic.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arithmetic

Examen de problemas simples de aritmética.
Más información: <https://manned.org/arithmetic.6>.

- Inicia un examen de aritmética:

`arithmetic`

- Especifica uno o más símbolos de [o]peración aritmética para obtener problemas relacionados con ellos:

`arithmetic -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+|-|x|/</span>

- Especifica un rango. Los problemas de suma y multiplicación presentarán números entre 0 y el rango, inclusive. Los problemas de resta y división tendrán el resultado requerido y el número a operar, entre 0 y el rango:

`arithmetic -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>
