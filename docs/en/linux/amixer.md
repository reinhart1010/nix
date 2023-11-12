---
layout: page
title: linux/amixer (English)
description: "Mixer for ALSA soundcard driver."
content_hash: 3081594782cf2e66d374bcbf6b75f521d596c9bd
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/amixer.html
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

Mixer for ALSA soundcard driver.
More information: <https://manned.org/amixer>.

- Turn up the master volume by 10%:

`amixer -D pulse sset Master `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10%+</span>

- Turn down the master volume by 10%:

`amixer -D pulse sset Master `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10%-</span>
