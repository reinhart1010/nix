---
layout: page
title: linux/tic (한국어)
description: "terminfo를 컴파일하고 ncurses에 설치합니다."
content_hash: 040bf41ce4e117916e4aecd104f602eea851df0c
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/tic.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tic

terminfo를 컴파일하고 ncurses에 설치합니다.
더 많은 정보: <https://pubs.opengroup.org/onlinepubs/007908799/xcurses/terminfo.html>.

- 터미널에 대한 terminfo를 컴파일하고 설치:

`tic -xe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">터미널</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/터미널.info</span>

- terminfo 파일의 오류 확인:

`tic -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/터미널.info</span>

- 데이터베이스 위치 출력:

`tic -D`
