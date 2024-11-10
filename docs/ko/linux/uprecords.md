---
layout: page
title: linux/uprecords (한국어)
description: "시스템의 역사적인 가동 시간 기록을 요약하여 표시합니다."
content_hash: 2fd57b7b4458fcdcffd71b0cf9ed135a43ee5e9e
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/uprecords.html
    icon: bi bi-globe
tldri18n_status: 2
---
# uprecords

시스템의 역사적인 가동 시간 기록을 요약하여 표시합니다.
더 많은 정보: <https://manned.org/uprecords>.

- 상위 10개의 역사적인 가동 시간 기록 요약 표시:

`uprecords`

- 상위 25개의 기록 표시:

`uprecords -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">25</span>

- 커널 버전 대신 재부팅 간의 다운타임 표시:

`uprecords -d`

- 가장 최근의 재부팅 내역 표시:

`uprecords -B`

- 정보를 생략하지 않고 표시:

`uprecords -w`
