---
layout: page
title: common/nix3-repl (한국어)
description: "Nix 표현식을 평가하기 위한 대화형 환경 시작."
content_hash: 4a6b24426eb73b9f7b2bc84c63d96ed936730f5a
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/nix3-repl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nix3-repl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nix repl

Nix 표현식을 평가하기 위한 대화형 환경 시작.
Nix 표현식 언어에 대한 설명은 <https://nixos.org/manual/nix/stable/language/index.html>을 참고하세요.
더 많은 정보: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-repl.html>.

- Nix 표현식을 평가하기 위한 대화형 환경 시작:

`nix repl`

- 플레이크(예: `nixpkgs`)의 모든 패키지를 스코프로 불러오기:

`:lf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs</span>

- 표현식에서 패키지 빌드:

`:b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">표현식</span>

- 표현식에서 패키지를 사용할 수 있는 셸 시작:

`:u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">표현식</span>

- 표현식에서 패키지의 종속성을 사용할 수 있는 셸 시작:

`:s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">표현식</span>
