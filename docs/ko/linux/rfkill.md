---
layout: page
title: linux/rfkill (한국어)
description: "무선 장치를 활성화하거나 비활성화합니다."
content_hash: b7a11085bdee101adb5f8ff0bd487c99538131d6
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/rfkill.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rfkill

무선 장치를 활성화하거나 비활성화합니다.
더 많은 정보: <https://manned.org/rfkill>.

- 장치 나열:

`rfkill`

- 열로 필터링:

`rfkill -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ID,TYPE,DEVICE</span>

- 유형별로 장치 차단 (예: bluetooth, wlan):

`rfkill block `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bluetooth</span>

- 유형별로 장치 차단 해제 (예: bluetooth, wlan):

`rfkill unblock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan</span>

- JSON 형식으로 출력:

`rfkill -J`
