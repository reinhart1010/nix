---
layout: page
title: osx/csrutil (español)
description: "Gestiona la configuración de la Protección de Integridad del Sistema."
content_hash: 209faeba692e63eb5c2e3b31db943c3684887aa2
last_modified_at: 2024-01-07
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
Más información: <https://ss64.com/osx/csrutil.html>.

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
