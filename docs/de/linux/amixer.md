---
layout: page
title: linux/amixer (Deutsch)
description: "Mixer für den ALSA-Soundkarten-Treiber."
content_hash: 2259b37353443cb94045992942c9afd9045c8ecc
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/amixer.html
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

Mixer für den ALSA-Soundkarten-Treiber.
Weitere Informationen: <https://manned.org/amixer>.

- Erhöhe den Gesamtpegel um 10%:

`amixer -D pulse sset Master `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10%+</span>

- Verringere den Gesamtpegel um 10%:

`amixer -D pulse sset Master `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10%-</span>
