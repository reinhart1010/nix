---
layout: page
title: openbsd/df (한국어)
description: "파일 시스템 디스크 공간 사용량 개요를 표시합니다."
content_hash: 313c7c9e44eff50c2ce9c8147f53cc2103513c9b
last_modified_at: 2024-06-24
related_topics:
  - title: English version
    url: /en/openbsd/df.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/openbsd/df.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/openbsd/df.html
    icon: bi bi-globe
tldri18n_status: 2
---
# df

파일 시스템 디스크 공간 사용량 개요를 표시합니다.
더 많은 정보: <https://man.openbsd.org/df.1>.

- 모든 파일 시스템과 디스크 사용량을 512바이트 단위로 표시:

`df`

- [h]uman-readable 형식으로 모든 파일 시스템과 디스크 사용량 표시 (1024의 거듭 제곱에 기반):

`df -h`

- 지정된 파일 또는 디렉토리를 포함하는 파일 시스템 및 해당 디스크 사용량 표시:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 무료 및 사용 중인 [i]노드 수에 대한 통계 포함:

`df -i`

- 공간 수치 작성 시 1024바이트 단위 사용:

`df -k`

- [P]ortable 방식으로 정보 표시:

`df -P`
