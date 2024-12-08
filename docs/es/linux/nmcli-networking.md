---
layout: page
title: linux/nmcli-networking (español)
description: "Administra el estado de red de NetworkManager."
content_hash: e3c1595458f6fd1cc081b4f00c79477e7d2f4180
last_modified_at: 2024-12-08
related_topics:
  - title: English version
    url: /en/linux/nmcli-networking.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/nmcli-networking.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/nmcli-networking.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/nmcli-networking.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nmcli networking

Administra el estado de red de NetworkManager.
Este subcomando también se puede invocar con `nmcli n`.
Más información: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

- Muestra el estado de red de NetworkManager:

`nmcli networking`

- Activa o desactiva redes y todas las interfaces gestionadas por NetworkManager:

`nmcli networking `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Muestra el último estado de conectividad conocido:

`nmcli networking connectivity`

- Muestra el estado de conectividad actual:

`nmcli networking connectivity check`
