---
layout: page
title: common/radare2 (한국어)
description: "리버스 엔지니어링 도구 세트."
content_hash: 1acc99ef5aac86f6d7cf465fde158543293db454
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/radare2.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/radare2.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/radare2.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># radare2

리버스 엔지니어링 도구 세트.
더 많은 정보: <https://www.radare.org/r/docs.html>.

- 파일 형식 헤더를 파싱하지 않고 쓰기 모드로 파일 열기:

`radare2 -nw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>

- 프로그램 디버깅:

`radare2 -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>

- 대화형 CLI에 들어가기 전에 스크립트 실행:

`radare2 -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.r2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>

- 대화형 CLI에서 명령어에 대한 도움말 표시:

`> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">radare2_명령어</span>`?`

- 대화형 CLI에서 셀 명령어 실행:

`> !`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">셸_명령어</span>

- 현재 블록의 원시 바이트를 파일로 덤프:

`> pr > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.bin</span>
