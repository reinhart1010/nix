---
layout: page
title: common/brew (한국어)
description: "macOS와 Linux를 위한 패키지 관리자."
content_hash: 3cccdbbd66fd5d24f97af56f6ab0d21b8117ffef
related_topics:
  - title: English version
    url: /en/common/brew.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/brew.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/brew.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/brew.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/brew.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/brew.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/brew.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># brew

macOS와 Linux를 위한 패키지 관리자.
더 많은 정보: <https://brew.sh>.

- 공식(formula) 혹은 캐스크(cask)의 최신 안정 버전을 설치 (개발 버전을 원한다면 `--devel` 사용):

`brew install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula</span>

- 설치된 모든 공식(formulae)과 캐스크(casks) 나열:

`brew list`

- 설치된 특정 공식(formula) 혹은 캐스크(cask) 업그레이드 (옵션이 주어지지 않으면 모든 공식과 캐스크 업그레이드):

`brew upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula</span>

- Homebrew 저장소에서 Homebrew와 함께 모든 공식(formulae)과 캐스크(casks)의 최신 버전 가져오기:

`brew update`

- 최신 버전이 아닌 공식(formulae)과 캐스크(casks) 나열:

`brew outdated`

- 사용 가능한 공식(formulae)과 캐스크(casks) 검색:

`brew search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>

- 공식(formula) 혹은 캐스크(cask)에 대한 정보 표시 (버전, 설치 경로, 의존성 등):

`brew info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula</span>

- 설치된 Homebrew에 문제가 있는 확인:

`brew doctor`
