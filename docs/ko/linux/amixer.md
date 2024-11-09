---
layout: page
title: linux/amixer (한국어)
description: "ALSA 사운드 카드 드라이버의 믹서."
content_hash: 8a4a461a651c90fb8d2afeef0e7d7a615e190434
last_modified_at: 2024-11-09
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
  - title: 中文 version
    url: /zh/linux/amixer.html
    icon: bi bi-globe
tldri18n_status: 2
---
# amixer

ALSA 사운드 카드 드라이버의 믹서.
더 많은 정보: <https://manned.org/amixer>.

- 마스터 볼륨을 10% 높이기:

`amixer -D pulse sset Master `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10%+</span>

- 마스터 볼륨을 10% 낮추기:

`amixer -D pulse sset Master `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10%-</span>
