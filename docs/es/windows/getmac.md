---
layout: page
title: windows/getmac (español)
description: "Muestra las direcciones MAC de un sistema."
content_hash: 7309673545f0f044df8c815ed286f05029462e64
last_modified_at: 2023-07-08
related_topics:
  - title: English version
    url: /en/windows/getmac.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/getmac.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># getmac

Muestra las direcciones MAC de un sistema.
Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/getmac>.

- Muestra las direcciones MAC del sistema actual:

`getmac`

- Muestra los detalles en un formato específico:

`getmac /fo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table|list|csv</span>

- Excluye la cabecera en la lista de salida:

`getmac /nh`

- Muestra las direcciones MAC de un equipo remoto:

`getmac /s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_host</span>` /u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombredeusuario</span>` /p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contraseña</span>

- Muestra las direcciones MAC con información detallada:

`getmac /v`

- Muestra información de uso detallada:

`getmac /?`
