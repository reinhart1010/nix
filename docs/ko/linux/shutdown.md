---
layout: page
title: linux/shutdown (한국어)
description: "시스템 종료 및 재부팅."
content_hash: 091b209588ac70a444d0284d15d245d7dac4333e
last_modified_at: 2024-11-12
related_topics:
  - title: català version
    url: /ca/linux/shutdown.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/shutdown.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/shutdown.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/shutdown.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/shutdown.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/shutdown.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shutdown

시스템 종료 및 재부팅.
더 많은 정보: <https://manned.org/shutdown.8>.

- 즉시 전원 끄기 ([h]alt):

`shutdown -h now`

- 즉시 [r]재부팅:

`shutdown -r now`

- 5분 후 [r]재부팅:

`shutdown -r +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` &`

- 오후 1시에 종료하기 (24시간 [h] 형식 사용):

`shutdown -h 13:00`

- 보류 중인 종료/재부팅 작업 [c]취소:

`shutdown -c`
