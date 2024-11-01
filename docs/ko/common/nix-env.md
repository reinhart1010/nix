---
layout: page
title: common/nix-env (한국어)
description: "Nix 사용자 환경을 조작하거나 조회합니다."
content_hash: d3b0e7a43ca0886d7d1bba8107f00f9ab989027e
last_modified_at: 2024-11-01
related_topics:
  - title: Deutsch version
    url: /de/common/nix-env.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/nix-env.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nix-env.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nix-env

Nix 사용자 환경을 조작하거나 조회합니다.
더 많은 정보: <https://nixos.org/manual/nix/stable/#sec-nix-env>.

- 설치된 모든 패키지 나열:

`nix-env -q`

- 설치된 패키지 조회:

`nix-env -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색어</span>

- 사용 가능한 패키지 조회:

`nix-env -qa `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색어</span>

- 패키지 설치:

`nix-env -iA nixpkgs.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>

- URL에서 패키지 설치:

`nix-env -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>` --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 패키지 제거:

`nix-env -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>

- 특정 패키지 업그레이드:

`nix-env -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>

- 모든 패키지 업그레이드:

`nix-env -u`
