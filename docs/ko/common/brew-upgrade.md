---
layout: page
title: common/brew-upgrade (한국어)
description: "오래된 formulae 및 casks를 업그레이드."
content_hash: 58fa7b38d91ecc64b7623e86773c229264821bef
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/brew-upgrade.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/brew-upgrade.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># brew upgrade

오래된 formulae 및 casks를 업그레이드.
더 많은 정보: <https://docs.brew.sh/Manpage#upgrade-options-outdated_formulaoutdated_cask->.

- 모든 오래된 casks 및 formulae 업그레이드:

`brew upgrade`

- 특정 formula/cask를 업그레이드:

`brew upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula|cask</span>

- 업그레이드할 항목을 인쇄하되, 실제로는 아무것도 업그레이드 하지 않음 :

`brew upgrade --dry-run`
