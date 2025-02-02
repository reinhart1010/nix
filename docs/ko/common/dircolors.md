---
layout: page
title: common/dircolors (한국어)
description: "LS_COLOR 환경변수와 스타일 `ls`, `dir`, 등을 설정하기 위한 명령어들을 출력한다."
content_hash: 932c6ac827bc4f80397491e25744cadc8a76bf94
last_modified_at: 2024-12-22
related_topics:
  - title: English version
    url: /en/common/dircolors.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dircolors.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/dircolors.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dircolors

LS_COLOR 환경변수와 스타일 `ls`, `dir`, 등을 설정하기 위한 명령어들을 출력한다.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/dircolors-invocation.html>.

- 기본 색상을 사용하여 LS_COLOR를 설정하는 명령어들 출력하기:

`dircolors`

- 파일로부터 색상을 사용하여 LS_COLOR를 설정하는 명령어들 출력하기:

`dircolors `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>

- Bourne 쉘에 관한 명령어들 출력:

`dircolors --bourne-shell`

- C 쉘에 관한 명령어들 출력:

`dircolors --c-shell`

- 파일 유형과 확장에 대한 기본 색상들 보기:

`dircolors --print-data`
