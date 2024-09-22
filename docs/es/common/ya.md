---
layout: page
title: common/ya (español)
description: "Gestiona los paquetes y complementos de Yazi."
content_hash: 1e129510c3d3d163082924015e407e07cf7244a7
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/ya.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ya

Gestiona los paquetes y complementos de Yazi.
Más información: <https://github.com/sxyazi/yazi>.

- Añade un paquete:

`ya pack -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Actualiza todos los paquetes:

`ya pack -u`

- Suscribirse a los mensajes de todas las instancias remotas:

`ya sub `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tipos</span>

- Publica un mensaje en la instancia actual con cuerpo de cadena:

`ya pub --str `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena_mensaje</span>

- Publica un mensaje a la instancia actual con formato JSON:

`ya pub --json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mensaje_json</span>

- Publica un mensaje en la instancia especificada con una cadena de texto:

`ya pub-to --str `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mensaje</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">receptor</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tipo</span>
