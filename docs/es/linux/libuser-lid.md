---
layout: page
title: linux/libuser-lid (español)
description: "Muestra los grupos de un usuario o los usuarios de un grupo."
content_hash: 0bcbdec55d060c649d29625e104397c9a5639827
last_modified_at: 2024-11-16
related_topics:
  - title: English version
    url: /en/linux/libuser-lid.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/libuser-lid.html
    icon: bi bi-globe
tldri18n_status: 2
---
# libuser-lid

Muestra los grupos de un usuario o los usuarios de un grupo.
En Fedora y Arch Linux, este programa se instala como `lid`.
Más información: <https://manned.org/lid.8>.

- Lista los grupos primarios y secundarios de un usuario específico:

`sudo lid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>

- Lista los usuarios de un grupo específico:

`sudo lid --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>
