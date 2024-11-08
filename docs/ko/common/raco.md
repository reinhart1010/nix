---
layout: page
title: common/raco (한국어)
description: "Racket 명령줄 도구."
content_hash: b8cb04b400d717552a8b358dd459b852f95f484c
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/raco.html
    icon: bi bi-globe
tldri18n_status: 2
---
# raco

Racket 명령줄 도구.
더 많은 정보: <https://docs.racket-lang.org/raco/>.

- 패키지를 설치하고, 자동으로 의존성을 설치:

`raco pkg install --auto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_출처</span>

- 현재 디렉토리를 패키지로 설치:

`raco pkg install`

- 컬렉션에 대한 바이트코드, 문서, 실행 파일 및 메타데이터 색인 생성(또는 재생성):

`raco setup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컬렉션1 컬렉션2 ...</span>

- 파일 내 테스트 실행:

`raco test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/테스트1.rkt 경로/대상/테스트2.rkt ...</span>

- 로컬 문서 검색:

`raco docs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색어 ...</span>

- 도움말 표시:

`raco help`
