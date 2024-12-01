---
layout: page
title: linux/swww (español)
description: "Servicio (daemon) eficiente de fondos de pantalla animados para Wayland."
content_hash: 8cc6b7a8cbd58ef0360d56def5f44c0d445d7480
last_modified_at: 2024-12-01
related_topics:
  - title: English version
    url: /en/linux/swww.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/swww.html
    icon: bi bi-globe
tldri18n_status: 2
---
# swww

Servicio (daemon) eficiente de fondos de pantalla animados para Wayland.
Vea también: `swww-daemon`.
Más información: <https://github.com/LGFae/swww>.

- Establece fondo de pantalla:

`swww img `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen</span>

- Establece el fondo de pantalla en las salidas especificadas:

`swww img -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">salida1,salida2,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen</span>

- Restaura el último fondo de pantalla:

`swww restore`

- Apaga daemon:

`swww kill`

- Muestra información de salida:

`swww query`
