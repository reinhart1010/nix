---
layout: page
title: linux/boltctl (한국어)
description: "썬더볼트 장치를 제어합니다."
content_hash: d4fa3e3c76669212a40fba10b642a947a119282e
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/boltctl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/boltctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# boltctl

썬더볼트 장치를 제어합니다.
더 많은 정보: <https://manned.org/boltctl>.

- 연결된 (및 승인된) 장치 나열:

`boltctl`

- 승인되지 않은 장치를 포함하여 연결된 장치 나열:

`boltctl list`

- 장치를 일시적으로 승인:

`boltctl authorize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치_UUID</span>

- 장치를 승인하고 기억:

`boltctl enroll `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치_UUID</span>

- 이전에 승인된 장치 승인 취소:

`boltctl forget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치_UUID</span>

- 장치에 대한 추가 정보 표시:

`boltctl info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치_UUID</span>
