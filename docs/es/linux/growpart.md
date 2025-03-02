---
layout: page
title: linux/growpart (español)
description: "Extiende una partición en un disco o imagen de disco para llenar el espacio disponible."
content_hash: 856008e31b460bdc75e3288b809dfe17239225ec
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/growpart.html
    icon: bi bi-globe
tldri18n_status: 2
---
# growpart

Extiende una partición en un disco o imagen de disco para llenar el espacio disponible.
Más información: <https://github.com/canonical/cloud-utils>.

- Extiende la partición `n` desde `sdX` para llenar el espacio vacío hasta el final del disco o el principio de la siguiente partición:

`growpart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>

- Muestra qué modificaciones se harían al hacer crecer la partición `n` en una imagen de disco:

`growpart --dry-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/ruta/a/disco.img</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>
