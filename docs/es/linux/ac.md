---
layout: page
title: linux/ac (español)
description: "Imprime estadísticas sobre cuánto tiempo han estado conectados los usuarios."
content_hash: dc82569bbfa6f00d7bba42ffdf342b2eb3899ca9
last_modified_at: 2024-11-16
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
  - title: فارسی version
    url: /fa/linux/ac.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ac.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/ac.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/ac.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/ac.html
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
tldri18n_status: 2
---
# ac

Imprime estadísticas sobre cuánto tiempo han estado conectados los usuarios.
Más información: <https://www.gnu.org/software/acct/manual/accounting.html#ac>.

- Imprime cuánto tiempo ha estado conectado el usuario actual en horas:

`ac`

- Imprime cuánto tiempo han estado conectados los usuarios en horas:

`ac --individual-totals`

- Imprime cuánto tiempo ha estado conectado un usuario en particular en horas:

`ac --individual-totals `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>

- Imprime cuánto tiempo un usuario en particular ha estado conectado en horas por día (en total):

`ac --daily-totals --individual-totals `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>

- Muestra también detalles adicionales:

`ac --compatibility`
