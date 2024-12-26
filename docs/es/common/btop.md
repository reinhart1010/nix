---
layout: page
title: common/btop (español)
description: "Un monitor de recursos que muestra información sobre la CPU, memoria, discos, red y procesos."
content_hash: 0b2c47a22435fce02c7c29f51fbbf0dae3bfa02f
last_modified_at: 2024-12-26
related_topics:
  - title: English version
    url: /en/common/btop.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/btop.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/btop.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/btop.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># btop

Un monitor de recursos que muestra información sobre la CPU, memoria, discos, red y procesos.
Una versión C++ de `bpytop`.
Más información: <https://github.com/aristocratos/btop>.

- Inicia `btop`:

`btop`

- Inicia `btop` con la configuración especificada:

`btop --preset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0..9</span>

- Inicia `btop` en modo TTY usando 16 colores y símbolos gráficos compatibles con TTY:

`btop --tty_on`

- Inicia `btop` en modo 256 colores en lugar de 24 bits:

`btop --low-color`

- Establece la tasa de actualización a 500 milisegundos:

`btop --update 500`
