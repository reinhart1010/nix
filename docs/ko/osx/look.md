---
layout: page
title: osx/look (한국어)
description: "정렬된 파일에서 특정 접두사로 시작하는 줄을 표시합니다."
content_hash: 29d837dba3e3668865bb750121e27cc6fb2db9e4
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/look.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/look.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/look.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/look.html
    icon: bi bi-globe
tldri18n_status: 2
---
# look

정렬된 파일에서 특정 접두사로 시작하는 줄을 표시합니다.
같이 보기: `grep`, `sort`.
더 많은 정보: <https://keith.github.io/xcode-man-pages/look.1.html>.

- 특정 파일에서 특정 접두사로 시작하는 줄 검색:

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">접두사</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 대소문자를 구분하지 않고 영숫자 문자만 검색:

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--ignore-case</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--alphanum</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">접두사</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 문자열 종료 문자를 지정 (기본값은 공백):

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--terminate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>

- `/usr/share/dict/words`에서 검색 (`--ignore-case` 및 `--alphanum` 기본 적용):

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">접두사</span>
