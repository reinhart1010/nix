---
layout: page
title: linux/nmcli-general (español)
description: "Administra los ajustes generales de NetworkManager."
content_hash: 2d0c5a89e39e714d0b7864109588bad49264401b
last_modified_at: 2024-12-08
related_topics:
  - title: English version
    url: /en/linux/nmcli-general.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/nmcli-general.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/nmcli-general.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/nmcli-general.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nmcli general

Administra los ajustes generales de NetworkManager.
Este subcomando también se puede invocar con `nmcli g`.
Más información: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

- Muestra el estado general de NetworkManager:

`nmcli general`

- Muestra el nombre del host del dispositivo actual:

`nmcli general hostname`

- Cambia el nombre del host del dispositivo actual:

`sudo nmcli general hostname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nuevo_nombre</span>

- Muestra los permisos de NetworkManager:

`nmcli general permissions`

- Muestra el nivel actual de registro (logging) y los dominios:

`nmcli general logging`

- Establece el nivel de registro y/o dominios (mira `man NetworkManager.conf` para todos los dominios disponibles):

`nmcli general logging level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">INFO|OFF|ERR|WARN|DEBUG|TRACE</span>` domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dominio_1,dominio_2,...</span>
