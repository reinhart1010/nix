---
layout: page
title: common/ghcup (한국어)
description: "Haskell 툴체인을 설치 도우미."
content_hash: bd470b4d7da5c7076a3a62b9d664cf9be483248b
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/ghcup.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ghcup.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ghcup.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ghcup

Haskell 툴체인을 설치 도우미.
Haskell 툴체인을 설치, 관리, 업데이트.
더 많은 정보: <https://gitlab.haskell.org/haskell/ghcup-hs>.

- 대화형 TUI을 시작:

`ghcup tui`

- 사용 가능한 GHC/cabal 버전 목록 나열:

`ghcup list`

- 권장 GHC 버전 설치:

`ghcup install ghc`

- 특정 GHC 버전 설치:

`ghcup install ghc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 현재 "활성" GHC 버전을 설정:

`ghcup set ghc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- cabal을 설치:

`ghcup install cabal`

- `ghcup` 자체를 업데이트:

`ghcup upgrade`
