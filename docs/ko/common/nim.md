---
layout: page
title: common/nim (한국어)
description: "Nim 컴파일러."
content_hash: 790a16bf98a5fb771bc87e8a5dbadbaada35bdc9
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/nim.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nim

Nim 컴파일러.
Nim 언어 소스 파일을 처리, 컴파일 및 링크합니다.
더 많은 정보: <https://nim-lang.org/docs/nimc.html>.

- 소스 파일 컴파일:

`nim compile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.nim</span>

- 소스 파일 컴파일 및 실행:

`nim compile -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.nim</span>

- 릴리스 최적화가 활성화된 상태로 소스 파일 컴파일:

`nim compile -d:release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.nim</span>

- 파일 크기 최적화가 적용된 릴리스 바이너리 빌드:

`nim compile -d:release --opt:size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.nim</span>

- 모듈에 대한 HTML 문서 생성 (출력은 현재 디렉토리에 저장됨):

`nim doc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.nim</span>

- 파일의 문법 및 의미 체계 검사:

`nim check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.nim</span>
