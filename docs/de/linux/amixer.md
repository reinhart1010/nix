---
layout: page
title: linux/amixer (Deutsch)
description: "Mixer für den ALSA-Soundkarten-Treiber."
content_hash: 2259b37353443cb94045992942c9afd9045c8ecc
related_topics:
  - title: English version
    url: /en/linux/amixer.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/amixer.html
    icon: bi bi-globe
---
# amixer

Mixer für den ALSA-Soundkarten-Treiber.
Weitere Informationen: <https://manned.org/amixer>.

- Erhöhe den Gesamtpegel um 10%:

`amixer -D pulse sset Master `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10%+</span>

- Verringere den Gesamtpegel um 10%:

`amixer -D pulse sset Master `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10%-</span>
