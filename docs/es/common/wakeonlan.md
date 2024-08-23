---
layout: page
title: common/wakeonlan (español)
description: "Envía paquetes a los PCs habilitados para wake-on-LAN (WOL)."
content_hash: a737cc8c5f74064d20155e1ed4e4ddbb4ca62bda
last_modified_at: 2024-08-23
related_topics:
  - title: English version
    url: /en/common/wakeonlan.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wakeonlan

Envía paquetes a los PCs habilitados para wake-on-LAN (WOL).
Más información: <https://github.com/jpoliv/wakeonlan>.

- Envía paquetes a todos los dispositivos de la red local (255.255.255.255) especificando una dirección MAC:

`wakeonlan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">01:02:03:04:05:06</span>

- Envía paquete a un dispositivo específico a través de una dirección IP:

`wakeonlan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">01:02:03:04:05:06</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2</span>

- Imprime los comandos, pero no los ejecutes (dry-run):

`wakeonlan -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">01:02:03:04:05:06</span>

- Ejecuta en modo silencioso:

`wakeonlan -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">01:02:03:04:05:06</span>
