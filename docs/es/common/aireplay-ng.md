---
layout: page
title: common/aireplay-ng (español)
description: "Inyecta paquetes en una red inalámbrica."
content_hash: 6b08d51c4ad779f84d76ca7c5b85a78160b079e6
last_modified_at: 2023-02-21
related_topics:
  - title: English version
    url: /en/common/aireplay-ng.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aireplay-ng

Inyecta paquetes en una red inalámbrica.
Parte de `aircrack-ng`.
Más información: <https://www.aircrack-ng.org/doku.php?id=aireplay-ng>.

- Envía una cantidad específica de paquetes disociados dada la dirección MAC de un punto de acceso, la dirección MAC de un cliente y una interfaz:

`sudo aireplay-ng --deauth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cantidad</span>` --bssid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_punto_acceso</span>` --dmac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_cliente</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interfaz</span>
