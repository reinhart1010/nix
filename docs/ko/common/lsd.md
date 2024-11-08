---
layout: page
title: common/lsd (한국어)
description: "디렉터리 내용 목록."
content_hash: 3e5be6e9fac09d1cfd66d8f10f9f2b01d21f510e
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/lsd.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/lsd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lsd

디렉터리 내용 목록.
Rust로 작성된 차세대 `ls` 명령어.
더 많은 정보: <https://github.com/Peltoche/lsd>.

- 파일과 디렉터리를 한 줄에 하나씩 나열:

`lsd -1`

- 현재 디렉터리의 모든 파일과 디렉터리(숨김 파일 포함) 나열:

`lsd -a`

- 디렉터리 이름에 `/`를 추가하여 파일과 디렉터리 나열:

`lsd -F`

- 파일과 디렉터리를 긴 형식으로 나열 (권한, 소유권, 사람이 읽기 쉬운 형식의 크기, 수정 날짜 포함):

`lsd -lha`

- 파일과 디렉터리를 크기별로 내림차순 정렬하여 긴 형식으로 나열:

`lsd -lS`

- 파일과 디렉터리를 수정 날짜별로 오래된 것부터 정렬하여 긴 형식으로 나열:

`lsd -ltr`

- 디렉터리만 나열:

`lsd -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*/</span>

- 모든 디렉터리를 재귀적으로 트리 형식으로 나열:

`lsd --tree -d`
