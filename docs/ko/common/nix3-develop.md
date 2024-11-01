---
layout: page
title: common/nix3-develop (한국어)
description: "파생물의 빌드 환경을 제공하는 Bash 셸 실행."
content_hash: acefc179a0429436fba997e2a8c09a122d1b04dc
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/nix3-develop.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nix3-develop.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nix develop

파생물의 빌드 환경을 제공하는 Bash 셸 실행.
더 많은 정보: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-develop.html>.

- nixpkgs의 모든 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` 종속성을 사용하여 셸 시작:

`nix develop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs#pkg</span>

- 현재 디렉토리의 플레이크에 있는 기본 패키지에 대한 개발 셸 시작:

`nix develop`

- 해당 셸에서 소스 구성 및 빌드:

`configurePhase; buildPhase`
