---
layout: page
title: common/nix3-shell (한국어)
description: "지정된 패키지가 사용 가능한 셸 시작."
content_hash: 18b181db412f910b4af1f15f2cc70601f5b16c88
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/nix3-shell.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nix3-shell.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nix shell

지정된 패키지가 사용 가능한 셸 시작.
같이 보기: 개발 환경 설정을 위한 `nix-shell`, 플레이크에 대한 정보를 위한 `nix3 flake`.
더 많은 정보: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-shell.html>.

- `nixpkgs`의 일부 패키지와 함께 대화형 셸 시작:

`nix shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs#pkg1 nixpkgs#packageSet.pkg2 ...</span>

- `nixpkgs`의 이전 버전(21.05)에서 제공하는 패키지로 셸 시작:

`nix shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs/nixos-21.05#pkg</span>

- 현재 디렉터리의 플레이크에서 "기본 패키지"와 함께 셸 시작, 빌드가 발생하면 빌드 로그 출력:

`nix shell -L`

- GitHub의 플레이크에서 패키지와 함께 셸 시작:

`nix shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">github:소유자/레포#pkg</span>

- 패키지와 함께 셸에서 명령 실행:

`nix shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs#pkg</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아무개_셸 --아무개_플래그 '다른 아무개 인수들'</span>
