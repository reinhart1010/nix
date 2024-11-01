---
layout: page
title: common/nix3-search (한국어)
description: "Nix 플레이크에서 패키지를 검색."
content_hash: f36d881ea1d81bde501375bc495ca879cd18a4c5
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/nix3-search.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nix3-search.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nix search

Nix 플레이크에서 패키지를 검색.
같이 보기: 플레이크에 대한 정보는 `nix3 flake`.
더 많은 정보: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-search.html>.

- `nixpkgs`에서 이름이나 설명을 기반으로 패키지 검색:

`nix search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_어구...</span>

- nixpkgs에서 패키지 설명 표시:

`nix search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs#패키지</span>

- github에서 플레이크로부터 사용할 수 있는 모든 패키지 표시:

`nix search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">github:소유자/레포</span>
