---
layout: page
title: linux/nmcli-connection (español)
description: "Gestiona conexiones con NetworkManager."
content_hash: 6fe4dfe2aab542691831d41f792cd52efc25d72d
last_modified_at: 2024-12-08
related_topics:
  - title: English version
    url: /en/linux/nmcli-connection.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/nmcli-connection.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/nmcli-connection.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/nmcli-connection.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/nmcli-connection.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nmcli connection

Gestiona conexiones con NetworkManager.
Este subcomando puede invocarse también con `nmcli c`.
Más información: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

- Lista todas las conexiones NetworkManager (muestra nombre, UUID, tipo y dispositivo):

`nmcli connection`

- Activa una conexión:

`nmcli connection up uuid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid</span>

- Desactiva una conexión:

`nmcli connection down uuid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid</span>

- Crea una conexión de doble pila autoconfigurada:

`nmcli connection add ifname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_interfaz</span>` type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ethernet</span>` ipv4.method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">auto</span>` ipv6.method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">auto</span>

- Crea una conexión estática exclusivamente IPv6:

`nmcli connection add ifname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_interfaz</span>` type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ethernet</span>` ip6 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2001:db8::2/64</span>` gw6 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2001:db8::1</span>` ipv6.dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2001:db8::1</span>` ipv4.method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ignore</span>

- Crea una conexión estática exclusivamente IPv4:

`nmcli connection add ifname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_interfaz</span>` type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ethernet</span>` ip4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.7/8</span>` gw4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.1</span>` ipv4.dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.1</span>` ipv6.method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ignore</span>

- Crea una conexión VPN usando OpenVPN desde un archivo OVPN:

`nmcli connection import type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">openvpn</span>` file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/configuración_vpn.ovpn</span>
