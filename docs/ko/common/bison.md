---
layout: page
title: common/bison (한국어)
description: "GNU 파서 생성기."
content_hash: f03e5cb93f3a69954a5fe462ecad674d0f507d6d
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/bison.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bison

GNU 파서 생성기.
더 많은 정보: <https://www.gnu.org/software/bison/>.

- bison 정의 파일을 컴파일:

`bison `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/file.y</span>

- 디버그 모드에서 컴파일하면, 결과 파서가 `stdout`에 추가 정보를 쓰게 됨:

`bison --debug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/file.y</span>

- 출력 파일 이름 지정:

`bison --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/output.c</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/file.y</span>

- 컴파일할 때 세세한 정보를 같이 출력:

`bison --verbose`
