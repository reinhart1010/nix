---
layout: page
title: common/nix3-edit (한국어)
description: "Nix 패키지의 Nix 표현을 $EDITOR에서 엽니다."
content_hash: 38d32df2ae0da297b88746bf1ddae029f87b5f73
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/nix3-edit.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nix3-edit.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nix edit

Nix 패키지의 Nix 표현을 $EDITOR에서 엽니다.
더 많은 정보: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-edit.html>.

- nixpkgs에서 패키지의 Nix 표현 소스를 `$EDITOR`에서 열기:

`nix edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs#패키지</span>

- 패키지의 소스를 `stdout`으로 덤프:

`EDITOR=cat nix edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs#패키지</span>
