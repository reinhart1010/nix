---
layout: page
title: osx/csrutil (español)
description: "Gestiona la configuración de la Protección de Integridad del Sistema."
content_hash: 4592e30d9fb91db0d273e361b5e5151158657480
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/csrutil.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/csrutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# csrutil

Gestiona la configuración de la Protección de Integridad del Sistema.
Más información: <https://keith.github.io/xcode-man-pages/csrutil.8.html>.

- Muestra el estado de la Protección de Integridad del Sistema:

`csrutil status`

- Desactiva la Protección de Integridad del Sistema:

`csrutil disable`

- Activa la Protección de Integridad del Sistema:

`csrutil enable`

- Muestra la lista de fuentes NetBoot permitidas:

`csrutil netboot list`

- Añade una dirección IPv4 a la lista de fuentes NetBoot permitidas:

`csrutil netboot add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>

- Restablece el estado de Protección de integridad del Sistema y borra la lista NetBoot:

`csrutil clear`
