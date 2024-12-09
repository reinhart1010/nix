---
layout: page
title: linux/nmcli-device (español)
description: "Gestiona interfaces de red y establece nuevas conexiones WiFi usando NetworkManager."
content_hash: 33b161b5982aa66a4ba329238e2c891ed6c4655d
last_modified_at: 2024-12-09
related_topics:
  - title: English version
    url: /en/linux/nmcli-device.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/nmcli-device.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/nmcli-device.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/nmcli-device.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nmcli device

Gestiona interfaces de red y establece nuevas conexiones WiFi usando NetworkManager.
Este subcomando también puede llamarse con `nmcli d`.
Más información: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

- Muestra los estados de todas las interfaces de red:

`nmcli device status`

- Muestra los puntos de acceso WiFi disponibles:

`nmcli device wifi`

- Se conecta a una red WiFi con el SSID especificado (se te pedirá una contraseña):

`nmcli --ask device wifi connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssid</span>

- Muestra la contraseña y el código QR para la red WiFi actual:

`nmcli device wifi show-password`
