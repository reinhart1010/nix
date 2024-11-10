---
layout: page
title: linux/pasuspender (한국어)
description: "다른 명령이 실행되는 동안 `pulseaudio`를 일시 중지하여 alsa에 접근할 수 있도록 합니다."
content_hash: 2c5ac75667421eb982004c8695d0ecb1c3e306be
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/pasuspender.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pasuspender

다른 명령이 실행되는 동안 `pulseaudio`를 일시 중지하여 alsa에 접근할 수 있도록 합니다.
더 많은 정보: <https://manned.org/pasuspender>.

- `jackd`를 실행하는 동안 PulseAudio 일시 중지:

`pasuspender -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jackd -d alsa --device hw:0</span>
