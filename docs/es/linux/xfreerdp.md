---
layout: page
title: linux/xfreerdp (español)
description: "Implementación del protocolo del Free Remote Desktop."
content_hash: 0a4f7f9893de0cdfb0cedcf86b6d9d12cd44a8b5
last_modified_at: 2024-10-20
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

Implementación del protocolo del Free Remote Desktop.
Más información: <https://www.freerdp.com>.

- Conéctate a un servidor FreeRDP:

`xfreerdp /u:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_usuario</span>` /p:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contraseña</span>` /v:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_ip</span>

- Conéctate a un servidor FreeRDP y activa la redirección de la salida de audio mediante el dispositivo `sys:alsa`:

`xfreerdp /u:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_usuario</span>` /p:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contraseña</span>` /v:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_ip</span>` /sound:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sys:alsa</span>

- Conéctate a un servidor FreeRDP con resolución dinámica:

`xfreerdp /v:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_ip</span>` /u:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_usuario</span>` /p:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contraseña</span>` /dynamic-resolution`

- Conéctate a un servidor FreeRDP con redirección del portapapeles:

`xfreerdp /v:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_ip</span>` /u:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_usuario</span>` /p:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contraseña</span>` +clipboard`

- Conéctate a un servidor FreeRDP ignorando cualquier comprobación de certificado:

`xfreerdp /v:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_ip</span>` /u:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_usuario</span>` /p:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contraseña</span>` /cert:ignore`

- Conéctate a un servidor FreeRDP con un directorio compartido:

`xfreerdp /v:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_ip</span>` /u:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_usuario</span>` /p:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contraseña</span>` /drive:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_compartido</span>
