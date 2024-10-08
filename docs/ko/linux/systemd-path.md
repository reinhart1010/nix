---
layout: page
title: linux/systemd-path (한국어)
description: "시스템 및 사용자 경로를 나열하고 조회."
content_hash: fa79dbd846dc86f9f88ba58c0223fc2ef7c36ce3
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/linux/systemd-path.html
    icon: bi bi-globe
tldri18n_status: 2
---
# systemd-path

시스템 및 사용자 경로를 나열하고 조회.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-path.html>.

- 알려진 경로와 현재 값을 나열:

`systemd-path`

- 지정된 경로를 조회하고 값을 표시:

`systemd-path "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로_이름</span>`"`

- 출력된 경로에 <span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suffix_string</span> 접미사를 추가:

`systemd-path --suffix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suffix_string</span>

- 짧은 버전 문자열을 출력하고 종료:

`systemd-path --version`
