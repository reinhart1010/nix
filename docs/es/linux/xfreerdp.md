---
layout: page
title: linux/xfreerdp (español)
description: "Implementación libre del protocolo de escritorio remoto (_Remote Desktop Protocol_)."
content_hash: 8e7aba04b77f4be1beaf468ba08df2747336a87a
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/xfreerdp.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/xfreerdp.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># xfreerdp

Implementación libre del protocolo de escritorio remoto (_Remote Desktop Protocol_).
Más información: <https://www.freerdp.com>.

- Conecta con un servidor FreeRDP:

`xfreerdp /u:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_usuario</span>` /p:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contraseña</span>` /v:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">direccion_ip</span>
