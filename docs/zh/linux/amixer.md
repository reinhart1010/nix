---
layout: page
title: linux/amixer (中文)
description: "ALSA 声卡驱动程序的混合器。"
content_hash: 52084980d0205ebc2c3305629ed037722a3a855a
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/amixer.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/amixer.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/amixer.html
    icon: bi bi-globe
tldri18n_status: 2
---
# amixer

ALSA 声卡驱动程序的混合器。
更多信息：<https://manned.org/amixer>.

- 增加 10% 的主音量：

`amixer -D pulse sset Master `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10%+</span>

- 降低 10% 的主音量：

`amixer -D pulse sset Master `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10%-</span>
