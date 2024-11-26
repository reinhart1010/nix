---
layout: page
title: linux/hyprctl (español)
description: "Controla partes del compositor Hyprland Wayland."
content_hash: 07e915c8d8f27e3cfce93473f25592be548883e0
last_modified_at: 2024-11-26
related_topics:
  - title: English version
    url: /en/linux/hyprctl.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/hyprctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hyprctl

Controla partes del compositor Hyprland Wayland.
Más información: <https://wiki.hyprland.org/Configuring/Using-hyprctl>.

- Recarga la configuración de Hyprland:

`hyprctl reload`

- Muestra el nombre de la ventana activa:

`hyprctl activewindow`

- Lista todos los dispositivos de entrada conectados:

`hyprctl devices`

- Lista todas las salidas con sus respectivas propiedades:

`hyprctl workspaces`

- Llama a un despachador:

`hyprctl dispatch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">despachador</span>

- Establece una configuración de una palabra clave (keyword) de forma dinámica:

`hyprctl keyword `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palabra_clave</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>

- Muestra versión:

`hyprctl version`
