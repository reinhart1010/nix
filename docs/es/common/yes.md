---
layout: page
title: common/yes (español)
description: "Retorna algo repetidamente."
content_hash: 97ca780828d1a46948e7cd62b2b931bb014e0c4d
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/yes.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/yes.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/yes.html
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
  - title: 中文 version
    url: /zh/common/yes.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yes

Retorna algo repetidamente.
Este comando es frecuentemente utilizado para aceptar todas las confirmaciones en comandos de instalación (como apt-get).
Más información: <https://www.gnu.org/software/coreutils/manual/html_node/yes-invocation.html>.

- Retorna repetidamente "mensaje":

`yes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mensaje</span>

- Retorna repetidamente "y":

`yes`

- Acepta todas las confirmaciones que muestre el comando `apt-get`:

`yes | sudo apt-get install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programa</span>

- Retorna repetidamente una nueva línea para aceptar siempre la opción predeterminada de una pregunta (prompt):

`yes ''`
