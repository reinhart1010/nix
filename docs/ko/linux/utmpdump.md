---
layout: page
title: linux/utmpdump (한국어)
description: "btmp, utmp 및 wtmp 회계 파일을 덤프하고 로드합니다."
content_hash: 7723133ad55561a2d498c09afdee48825f0b0fd5
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/utmpdump.html
    icon: bi bi-globe
tldri18n_status: 2
---
# utmpdump

btmp, utmp 및 wtmp 회계 파일을 덤프하고 로드합니다.
더 많은 정보: <https://manned.org/utmpdump>.

- `/var/log/wtmp` 파일을 일반 텍스트로 `stdout`에 덤프:

`utmpdump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/var/log/wtmp</span>

- 이전에 덤프한 파일을 `/var/log/wtmp`에 로드:

`utmpdump -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">덤프파일</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/var/log/wtmp</span>
