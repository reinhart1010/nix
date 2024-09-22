---
layout: page
title: common/brew-install (한국어)
description: "Homebrew formuale이나 cask를 설치."
content_hash: cd151b1c37fb631de7da031a5ec5b636149e9118
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/brew-install.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/brew-install.html
    icon: bi bi-globe
tldri18n_status: 2
---
# brew install

Homebrew formuale이나 cask를 설치.
더 많은 정보: <https://docs.brew.sh/Manpage#install-options-formulacask->.

- formuale/cask 설치:

`brew install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula|cask</span>

- 소스에서 formuale을 빌드하고 설치 (의존성은 여전히 병에서 설치):

`brew install --build-from-source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula</span>

- 매니페스트를 다운로드하고, 설치될 항목을 인쇄하지만 실제로는 아무것도 설치하지 않음:

`brew install --dry-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula|cask</span>
