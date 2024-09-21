---
layout: page
title: common/brew-outdated (한국어)
description: "오래된 casks와 formulae를 나열."
content_hash: 1bff38abe942b0decb0948d400a25142800c7faa
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/brew-outdated.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/brew-outdated.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># brew outdated

오래된 casks와 formulae를 나열.
모든 것을 업그레이드하려면, `brew upgrade`를 사용.
더 많은 정보: <https://docs.brew.sh/Manpage#outdated-options-formulacask->.

- 오래된 casks와 formulae를 모두 나열:

`brew outdated`

- 오직 오래된 formulae만 나열:

`brew outdated --formula`

- 오직 오래된 casks를 나열:

`brew outdated --cask`
