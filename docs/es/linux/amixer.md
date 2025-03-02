---
layout: page
title: linux/amixer (español)
description: "Mezclador para el controlador de tarjeta de sonido ALSA."
content_hash: 466af2383db4726d7589e87c629909c326149846
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/linux/amixer.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/amixer.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/amixer.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/amixer.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/amixer.html
    icon: bi bi-globe
tldri18n_status: 2
---
# amixer

Mezclador para el controlador de tarjeta de sonido ALSA.
Más información: <https://manned.org/amixer>.

- Aumenta el volumen maestro en un 10%:

`amixer -D pulse sset Master `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10%+</span>

- Disminuye el volumen maestro en un 10%:

`amixer -D pulse sset Master `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10%-</span>
