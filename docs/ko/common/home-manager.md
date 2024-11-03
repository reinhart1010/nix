---
layout: page
title: common/home-manager (한국어)
description: "Nix를 이용하여 사용자 환경을 관리."
content_hash: 75a7a5f273ec823221d73d4b7e58ce018bc6f455
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/home-manager.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/home-manager.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># home-manager

Nix를 이용하여 사용자 환경을 관리.
더 많은 정보: <https://github.com/rycee/home-manager>.

- `~/.config/nixpkgs/home.nix`에 정의된 구성을 활성화:

`home-manager build`

- 구성을 활성화하고 해당 구성으로 전환:

`home-manager switch`
