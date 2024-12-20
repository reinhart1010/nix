---
layout: page
title: linux/nmcli-radio (español)
description: "Muestra el estado de los interruptores de radio o activa/desactiva utilizando NetworkManager."
content_hash: 1b5d5b21595469425a8dadbeb14ddb6cc36912ec
last_modified_at: 2024-12-09
related_topics:
  - title: English version
    url: /en/linux/nmcli-radio.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/nmcli-radio.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/nmcli-radio.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nmcli radio

Muestra el estado de los interruptores de radio o activa/desactiva utilizando NetworkManager.
Este subcomando también puede llamarse con `nmcli r`.
Más información: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

- Muestra el estado de WiFi:

`nmcli radio wifi`

- Enciende o apaga WiFi:

`nmcli radio wifi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Muestra el estado de WWAN:

`nmcli radio wwan`

- Enciende o apaga WWAN:

`nmcli radio wwan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Muestra el estado de todos los interruptores:

`nmcli radio all`

- Activa o apaga todos los interruptores:

`nmcli radio all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>
