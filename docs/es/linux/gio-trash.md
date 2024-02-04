---
layout: page
title: linux/gio-trash (español)
description: "Mueve archivos a la papelera."
content_hash: 81658c6dfeb6993372e2a1330aca3687d3176a83
last_modified_at: 2024-02-04
related_topics:
  - title: English version
    url: /en/linux/gio-trash.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gio trash

Mueve archivos a la papelera.
Usado por GNOME para manejar la papelera.
Más información: <https://manned.org/gio.1>.

- Mueve archivos específicos a la papelera:

`gio trash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_directorio1 ruta/al/archivo_o_directorio2 ...</span>

- Lista los elementos de la papelera:

`gio trash --list`

- Restaura un elemento específico de la papelera utilizando su identificador:

`gio trash trash://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador</span>
