---
layout: page
title: common/ac (español)
description: "Imprimir estadísticas sobre cuanto tiempo han estado conectados los usuarios."
content_hash: 2aa566b79fb03fd0a67a06501e8a7c854c7bd40d
related_topics:
  - title: English version
    url: /en/common/ac.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ac.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ac.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ac

Imprimir estadísticas sobre cuanto tiempo han estado conectados los usuarios.
Más información: <https://man.openbsd.org/ac>.

- Imprime cuanto tiempo ha estado conectado el usuario actual en horas:

`ac`

- Imprime cuanto tiempo han estado conectados los usuarios en horas:

`ac -p`

- Imprime cuanto tiempo ha estado conectado un usuario en particular en horas:

`ac -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_usuario</span>

- Imprime cuánto tiempo ha estado conectado un usuario en particular en horas por día (con total):

`ac -dp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_usuario</span>
