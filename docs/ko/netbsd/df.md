---
layout: page
title: netbsd/df (한국어)
description: "파일 시스템 디스크 공간 사용량 개요를 표시합니다."
content_hash: cef30488e8ba4e8b0d5f3929b891216aa823341a
last_modified_at: 2024-09-19
related_topics:
  - title: English version
    url: /en/netbsd/df.html
    icon: bi bi-globe
  - title: español version
    url: /es/netbsd/df.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/netbsd/df.html
    icon: bi bi-globe
tldri18n_status: 2
---
# df

파일 시스템 디스크 공간 사용량 개요를 표시합니다.
더 많은 정보: <https://man.netbsd.org/df.1>.

- 512바이트 단위로 모든 파일 시스템과 디스크 사용량 표시:

`df`

- [h]uman-readable 단위 사용 (1024의 거듭제곱에 기반):

`df -h`

- `statvfs`에 의해 반환된 구조체의 모든 필드 표시:

`df -G`

- 주어진 파일 또는 디렉토리를 포함하는 파일 시스템과 해당 디스크 사용량 표시:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 빈 및 사용중인 [i]노드의 통계 포함:

`df -i`

- 공간 값을 쓸 때 1024바이트 단위 사용:

`df -k`

- [P]ortable한 방식으로 정보 표시:

`df -P`
