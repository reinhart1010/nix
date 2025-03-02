---
layout: page
title: linux/addpart (español)
description: "Informa al kernel de Linux sobre la existencia de la partición especificada."
content_hash: d00aaff6e5fbeacd6a4a5788dfb8d3262514255b
last_modified_at: 2025-03-02
related_topics:
  - title: català version
    url: /ca/linux/addpart.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/addpart.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/addpart.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/addpart.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/addpart.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/addpart.html
    icon: bi bi-globe
tldri18n_status: 2
---
# addpart

Informa al kernel de Linux sobre la existencia de la partición especificada.
Es un envoltorio simple alrededor del ioctl `add partition`.
Más información: <https://manned.org/addpart>.

- Informa al kernel sobre la existencia de la partición especificada:

`addpart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dispositivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">partición</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">inicio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">longitud</span>
