---
layout: page
title: linux/w (한국어)
description: "로그인한 사용자와 그들의 프로세스를 표시합니다."
content_hash: 57d98153955b01ab8f4d690059b4ba1d63d294e9
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/w.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/w.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/w.html
    icon: bi bi-globe
tldri18n_status: 2
---
# w

로그인한 사용자와 그들의 프로세스를 표시합니다.
더 많은 정보: <https://www.geeksforgeeks.org/w-command-in-linux-with-examples/>.

- 현재 로그인한 모든 사용자에 대한 정보 표시:

`w`

- 특정 사용자에 대한 정보 표시:

`w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 헤더를 포함하지 않고 정보 표시:

`w --no-header`

- 로그인, JCPU 및 PCPU 열을 포함하지 않고 정보 표시:

`w --short`
