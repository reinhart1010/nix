---
layout: page
title: linux/ip-maddress (español)
description: "Gestiona direcciones multicast."
content_hash: 0da253b0de0dcbab2b01ce5734357c53493254f7
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/ip-maddress.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ip maddress

Gestiona direcciones multicast.
Más información: <https://manned.org/ip-maddress>.

- Lista las direcciones multicast y cuántos programas están suscritos a ellas:

`ip maddress`

- Lista de direcciones específicas de dispositivos:

`ip maddress show dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Se une a un grupo multicast estáticamente:

`sudo ip maddress add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">33:33:00:00:00:02</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Abandona un grupo multicast estático:

`sudo ip maddress delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">33:33:00:00:00:02</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>
