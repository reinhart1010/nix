---
layout: page
title: linux/abrt-action-analyze-c (한국어)
description: "`coredump`와 함께 문제 데이터 디렉터리에 대한 UUID를 계산합니다."
content_hash: 4e9e0b57f7ce1fa7f711a230544df5b2ee3fa2c7
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/abrt-action-analyze-c.html
    icon: bi bi-globe
tldri18n_status: 2
---
# abrt-action-analyze-c

`coredump`와 함께 문제 데이터 디렉터리에 대한 UUID를 계산합니다.
더 많은 정보: <https://manned.org/abrt-action-analyze-c>.

- 현재 작업 디렉터리에 대한 UUID 계산 및 저장:

`abrt-action-analyze-c`

- 특정 디렉터리에 대한 UUID 계산 및 저장:

`abrt-action-analyze-c -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 자세히 UUID 계산 및 저장:

`abrt-action-analyze-c -v`
