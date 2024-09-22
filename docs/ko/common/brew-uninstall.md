---
layout: page
title: common/brew-uninstall (한국어)
description: "Homebrew formula/cask를 제거."
content_hash: c3ebdefdae4ff1f211623e17d8db44123ddcf037
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/brew-uninstall.html
    icon: bi bi-globe
tldri18n_status: 2
---
# brew uninstall

Homebrew formula/cask를 제거.
나중에 사용하지 않는 의존성을 제거하려면, `brew autoremove`를 사용.
더 많은 정보: <https://docs.brew.sh/Manpage#uninstall-remove-rm-options-installed_formulainstalled_cask->.

- formula/cask를 설치 삭제:

`brew uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula|cask</span>

- cask를 제거하고 관련 파일을 모두 제거:

`brew uninstall --zap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cask</span>
