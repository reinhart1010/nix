---
layout: page
title: linux/nmtui (español)
description: "Interfaz de usuario de texto para controlar NetworkManager."
content_hash: b1cfa3e204cf7955d613c6b92147394262146a6d
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/nmtui.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/nmtui.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/nmtui.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/nmtui.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/nmtui.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nmtui

Interfaz de usuario de texto para controlar NetworkManager.
Utilice las teclas de flecha para navegar, tecla intro (enter) para seleccionar una opción.
Más información: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmtui.html>.

- Abre la interfaz de usuario:

`nmtui`

- Lista las conexiones disponibles, con la opción de activarlas o desactivarlas:

`nmtui connect`

- Se conecta a una red dada:

`nmtui connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre|uuid|dispositivo|SSID</span>

- Edita, añade, elimina una red determinada:

`nmtui edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre|identificador</span>

- Establece el nombre de la máquina (hostname) ante la red:

`nmtui hostname`
