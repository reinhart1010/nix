---
layout: page
title: linux/hyprpm (español)
description: "Complementos de control para el compositor Hyprland Wayland."
content_hash: 1f01ca3ef0c3b0f9a527c0da71ac1675f553822c
last_modified_at: 2024-07-01
related_topics:
  - title: English version
    url: /en/linux/hyprpm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/hyprpm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># hyprpm

Complementos de control para el compositor Hyprland Wayland.
Más información: <https://wiki.hyprland.org/Plugins/Using-Plugins/#hyprpm>.

- Añade un complemento:

`hyprpm add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_de_repositorio_git</span>

- Elimina un complemento:

`hyprpm remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_de_repositorio_git|nombre_del_complemento</span>

- Activa un complemento:

`hyprpm enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_complemento</span>

- Desactiva un complemento:

`hyprpm disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_complemento</span>

- Actualiza y comprueba todos los complementos:

`hyprpm update`

- Fuerza una operación:

`hyprpm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--force</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">operación</span>

- Lista todos los complementos instalados:

`hyprpm list`
