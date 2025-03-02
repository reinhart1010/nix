---
layout: page
title: linux/abrt-action-analyze-c (español)
description: "Calcula el UUID para un directorio de datos problemático con `coredump`."
content_hash: aff87a990805134fad971f5be4024240293b672b
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/abrt-action-analyze-c.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/abrt-action-analyze-c.html
    icon: bi bi-globe
tldri18n_status: 2
---
# abrt-action-analyze-c

Calcula el UUID para un directorio de datos problemático con `coredump`.
Más información: <https://manned.org/abrt-action-analyze-c>.

- Calcula y guarda el UUID para el directorio de trabajo actual:

`abrt-action-analyze-c`

- Calcula y guarda el UUID para un directorio específico:

`abrt-action-analyze-c -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Calcula y guarda el UUID de manera detallada:

`abrt-action-analyze-c -v`
