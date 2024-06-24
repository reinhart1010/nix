---
layout: page
title: freebsd/look (한국어)
description: "정렬된 파일에서 접두사로 시작하는 줄을 표시합니다."
content_hash: 550db176582acb4baa9a60789874138105bc5626
last_modified_at: 2024-06-24
related_topics:
  - title: English version
    url: /en/freebsd/look.html
    icon: bi bi-globe
  - title: español version
    url: /es/freebsd/look.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/freebsd/look.html
    icon: bi bi-globe
tldri18n_status: 2
---
# look

정렬된 파일에서 접두사로 시작하는 줄을 표시합니다.
같이 보기: `grep`, `sort`.
더 많은 정보: <https://man.freebsd.org/cgi/man.cgi?look>.

- 특정 파일에서 특정 접두사로 시작하는 줄을 검색:

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">접두사</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 알파벳과 숫자만 대소문자를 구분하지 않고 검색:

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--ignore-case</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--alphanum</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">접두사</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 종결 문자 지정 (기본값은 공백):

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--terminate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>

- `/usr/share/dict/words`에서 검색 (`--ignore-case` 및 `--alphanum`이 가정됨):

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">접두사</span>
