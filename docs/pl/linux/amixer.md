---
layout: page
title: linux/amixer (polski)
description: "Mikser dla sterownika ALSA kart dźwiękowych."
content_hash: 2795c6270f16fedaf3067c83e5470f4497be371a
related_topics:
  - title: Deutsch version
    url: /de/linux/amixer.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/amixer.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/amixer.html
    icon: bi bi-globe
---
# amixer

Mikser dla sterownika ALSA kart dźwiękowych.
Więcej informacji: <https://manned.org/amixer>.

- Zwiększenie głównego poziomu głośności o 10%:

`amixer -D pulse sset Master `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10%+</span>

- Zmniejszenie głównego poziomu głośności o 10%:

`amixer -D pulse sset Master `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10%-</span>
