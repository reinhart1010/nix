---
layout: page
title: linux/amixer (Deutsch)
description: "Mixer für den ALSA Soundkarten-Treiber."
content_hash: b7a9c896088af7cae95a41aa19d41c98d6b57158
related_topics:
  - title: English version
    url: /en/linux/amixer.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/amixer.html
    icon: bi bi-globe
---
# amixer

Mixer für den ALSA Soundkarten-Treiber.
Mehr Informationen: <https://manned.org/amixer>.

- Erhöhe den Gesamtpegel um 10%:

`amixer -D pulse sset Master `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10%+</span>

- Verringere den Gesamtpegel um 10%:

`amixer -D pulse sset Master `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10%-</span>
