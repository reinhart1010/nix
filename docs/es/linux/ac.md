---
layout: page
title: linux/ac (español)
description: "Imprime estadísticas sobre cuánto tiempo han estado conectados los usuarios."
content_hash: c2fa4413f400801952a44a9a3c60ec344f369de9
last_modified_at: 2023-03-21
related_topics:
  - title: català version
    url: /ca/linux/ac.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/ac.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/ac.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ac.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/ac.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/linux/ac.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/ac.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ac

Imprime estadísticas sobre cuánto tiempo han estado conectados los usuarios.
Más información: <https://www.gnu.org/software/acct/manual/accounting.html#ac>.

- Imprime cuánto tiempo ha estado conectado el usuario actual en horas:

`ac`

- Imprime cuánto tiempo han estado conectados los usuarios en horas:

`ac --individual-totals`

- Imprime cuánto tiempo ha estado conectado un usuario en particular en horas:

`ac --individual-totals `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_usuario</span>

- Imprime cuánto tiempo un usuario en particular ha estado conectado en horas por día (en total):

`ac --daily-totals --individual-totals `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_usuario</span>

- Muestra también detalles adicionales:

`ac --compatibility`
