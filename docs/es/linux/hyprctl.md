---
layout: page
title: linux/hyprctl (español)
description: "Controla partes del compositor Hyprland Wayland."
content_hash: 443c35a52f570b0671531ba233a97039cae3b20a
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/linux/hyprctl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/hyprctl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># hyprctl

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

- Llama a un gestor con un argumento:

`hyprctl dispatch exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aplicación</span>

- Establece una palabra clave de configuración de forma dinámica:

`hyprctl keyword `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palabra_clave</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>

- Muestra versión:

`hyprctl version`
