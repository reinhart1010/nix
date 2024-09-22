---
layout: page
title: common/brew-bundle (한국어)
description: "Homebrew, Homebrew Cask 및 Mac App Store용 번들러."
content_hash: baadc71afa15bc9ea652697baf4a0548ac40ca6a
last_modified_at: 2024-09-22
related_topics:
  - title: Deutsch version
    url: /de/common/brew-bundle.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/brew-bundle.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/brew-bundle.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/brew-bundle.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/brew-bundle.html
    icon: bi bi-globe
tldri18n_status: 2
---
# brew bundle

Homebrew, Homebrew Cask 및 Mac App Store용 번들러.
더 많은 정보: <https://github.com/Homebrew/homebrew-bundle>.

- 현재 경로의 Brewfile에서 패키지를 설치:

`brew bundle`

- 특정 경로의 특정 Brewfile에서 패키지를 설치:

`brew bundle --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 설치된 모든 패키지에서 Brewfile을 생성:

`brew bundle dump`

- Brewfile에 나열되지 않은 모든 공식을 제거:

`brew bundle cleanup --force`

- Brewfile에 설치하거나 업그레이드할 항목이 있는지 확인:

`brew bundle check`

- Brewfile의 모든 항목을 나열:

`brew bundle list --all`
