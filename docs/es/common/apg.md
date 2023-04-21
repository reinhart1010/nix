---
layout: page
title: common/apg (español)
description: "Crea contraseñas aleatorias arbitrariamente complejas."
content_hash: 7c25cbc28539408897d95b9a2eb72ffcb49faf80
last_modified_at: 2023-04-21
related_topics:
  - title: English version
    url: /en/common/apg.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/apg.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/apg.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/apg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/apg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/apg.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># apg

Crea contraseñas aleatorias arbitrariamente complejas.
Más información: <https://manned.org/apg>.

- Crea contraseñas aleatorias (la longitud predeterminada de la contraseña es 8):

`apg`

- Crea una contraseña con al menos 1 símbolo (S), 1 número (N), 1 mayúscula (C), 1 minúscula (L):

`apg -M SNCL`

- Crea una contraseña con 16 caracteres:

`apg -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16</span>

- Crea una contraseña con una longitud máxima de 16:

`apg -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16</span>

- Crea una contraseña que no aparece en un diccionario (se debe proporcionar el archivo del diccionario):

`apg -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_diccionario</span>
