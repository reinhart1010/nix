---
layout: page
title: common/fisher (한국어)
description: "Fish-shell 플러그인 관리자인 Fisher."
content_hash: 3ee1c16cc1b7137190b7e91fd6d9de0b80f918eb
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/fisher.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/fisher.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fisher

Fish-shell 플러그인 관리자인 Fisher.
이름별로 플러그인을 설치하거나 번들 설치의 경우 관리되는 'fishfile'에서 플러그인을 설치.
더 많은 정보: <https://github.com/jorgebucaran/fisher>.

- 하나 이상의 플러그인을 설치:

`fisher `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">플러그인1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">플러그인2</span>

- GitHub 요점에서 플러그인을 설치:

`fisher `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gist_url</span>

- 선호하는 편집기로 'fishfile'을 수동으로 편집하고 여러 플러그인을 설치:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">editor</span>` ~/.config/fish/fishfile; fisher`

- 설치된 플러그인 목록:

`fisher ls`

- 플러그인 업데이트:

`fisher update`

- 하나 이상의 플러그인을 제거:

`fisher remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">플러그인1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">플러그인2</span>
