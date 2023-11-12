---
layout: page
title: common/cabal (한국어)
description: "Haskell 패키지 인프라 (Cabal)에 대한 명령어 라인 인터페이스."
content_hash: b16ca0b1a88d3cbe29a8874da901f1e4474e6f9b
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/cabal.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cabal.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cabal.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/cabal.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cabal

Haskell 패키지 인프라 (Cabal)에 대한 명령어 라인 인터페이스.
Hackage 패키지 저장소에서 Haskell 프로젝트 및 Cabal패키지 관리.
더 많은 정보: <https://cabal.readthedocs.io/en/latest/intro.html>.

- Hackage에서 패키지 검색 및 리스트:

`cabal list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색할_문자열</span>

- 패키지에 대한 정보 출력:

`cabal info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>

- 패키지 다운로드 및 설치:

`cabal install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>

- 현재 디렉토리에서 새로운 Haskell 프로젝트 생성:

`cabal init`

- 현재 디렉토리에서 프로젝트 빌드:

`cabal build`

- 현재 디렉토리에서 프로젝트의 테스트 실행:

`cabal test`
