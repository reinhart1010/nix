---
layout: page
title: linux/abrt-action-analyze-backtrace (español)
description: "Analiza un backtrace de C/C++."
content_hash: 9930b23e768adad67430d763ae182bb7a6e16081
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/abrt-action-analyze-backtrace.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/abrt-action-analyze-backtrace.html
    icon: bi bi-globe
tldri18n_status: 2
---
# abrt-action-analyze-backtrace

Analiza un backtrace de C/C++.
Genera un hash de duplicación, una clasificación del backtrace e identifica la función que causó el fallo.
Guarda los datos como nuevos elementos `duphash`, `rating`, `crash_function` en el directorio del problema.
Más información: <https://manned.org/abrt-action-analyze-backtrace>.

- Analiza el backtrace para el directorio de trabajo actual:

`abrt-action-analyze-backtrace`

- Analiza el backtrace para un directorio específico:

`abrt-action-analyze-backtrace -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Analiza el backtrace de manera detallada:

`abrt-action-analyze-backtrace -v`
