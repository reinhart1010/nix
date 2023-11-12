---
layout: page
title: common/aireplay-ng (español)
description: "Inyecta paquetes en una red inalámbrica."
content_hash: 6b08d51c4ad779f84d76ca7c5b85a78160b079e6
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/common/aireplay-ng.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/aireplay-ng.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aireplay-ng.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/aireplay-ng.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/aireplay-ng.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/aireplay-ng.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aireplay-ng

Inyecta paquetes en una red inalámbrica.
Parte de `aircrack-ng`.
Más información: <https://www.aircrack-ng.org/doku.php?id=aireplay-ng>.

- Envía una cantidad específica de paquetes disociados dada la dirección MAC de un punto de acceso, la dirección MAC de un cliente y una interfaz:

`sudo aireplay-ng --deauth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cantidad</span>` --bssid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_punto_acceso</span>` --dmac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_cliente</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interfaz</span>
