---
layout: page
title: linux/iostat (Nederlands)
description: "Geeft statistieken weer voor apparaten en partities."
content_hash: aba0e8a96f73a83b9ffd15e66168d748ff78c9f4
last_modified_at: 2024-08-13
related_topics:
  - title: English version
    url: /en/linux/iostat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# iostat

Geeft statistieken weer voor apparaten en partities.
Meer informatie: <https://manned.org/iostat>.

- Toon een rapport van CPU- en schijfstatistieken sinds het opstarten van het systeem:

`iostat`

- Toon een rapport van CPU- en schijfstatistieken met eenheden omgezet naar megabytes:

`iostat -m`

- Toon CPU-statistieken:

`iostat -c`

- Toon schijfstatistieken met schijfnamen (inclusief LVM):

`iostat -N`

- Toon uitgebreide schijfstatistieken met schijfnamen voor apparaat "sda":

`iostat -xN `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sda</span>

- Toon incrementele rapporten van CPU- en schijfstatistieken elke 2 seconden:

`iostat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>
