---
layout: page
title: osx/csrutil (español)
description: "Gestionar la configuración de la Protección de Integridad del Sistema."
content_hash: 75a8ad7de67e6163700aae20cf3ad4cabff261b7
last_modified_at: 2023-08-13
related_topics:
  - title: English version
    url: /en/osx/csrutil.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/csrutil.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># csrutil

Gestionar la configuración de la Protección de Integridad del Sistema.
Más información: <https://ss64.com/osx/csrutil.html>.

- Mstra el estado de la Protección de Integridad del Sistema:

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