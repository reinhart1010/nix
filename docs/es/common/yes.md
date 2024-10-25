---
layout: page
title: common/yes (español)
description: "Retorna algo repetidamente."
content_hash: b53b003489577c4780ef90cce33d0fee0e08aaf9
last_modified_at: 2024-10-25
related_topics:
  - title: English version
    url: /en/common/yes.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/yes.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/yes.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/yes.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/yes.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/yes.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># yes

Retorna algo repetidamente.
Este comando es frecuentemente utilizado para aceptar todas las confirmaciones en comandos de instalación (como apt-get).
Más información: <https://www.gnu.org/software/coreutils/yes>.

- Retorna repetidamente "mensaje":

`yes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mensaje</span>

- Retorna repetidamente "y":

`yes`

- Acepta todas las confirmaciones que muestre el comando `apt-get`:

`yes | sudo apt-get install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programa</span>

- Retorna repetidamente una nueva línea para aceptar siempre la opción predeterminada de una pregunta (prompt):

`yes ''`
