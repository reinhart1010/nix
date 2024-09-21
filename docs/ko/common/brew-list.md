---
layout: page
title: common/brew-list (한국어)
description: "설치된 formulae 또는 cask 패키지 및 파일을 나열."
content_hash: 522df2347cbd32ac2d0e26fd12ad2555261d6eb7
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/brew-list.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/brew-list.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># brew list

설치된 formulae 또는 cask 패키지 및 파일을 나열.
더 많은 정보: <https://docs.brew.sh/Manpage#list-ls-options-installed_formulainstalled_cask->.

- 설치된 formulae 및 casks를 나열:

`brew list`

- 설치된 formula에 속하는 파일 목록:

`brew list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula</span>

- cask의 아티팩트 나열:

`brew list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cask</span>

- formulae만 출력:

`brew list --formula`

- casks만 출력:

`brew list --cask`
