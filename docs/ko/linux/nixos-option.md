---
layout: page
title: linux/nixos-option (한국어)
description: "NixOS 설정을 확인합니다."
content_hash: f191c225a4bce4ba24a9b425c1763551aa14a4e2
last_modified_at: 2024-11-09
related_topics:
  - title: Deutsch version
    url: /de/linux/nixos-option.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/nixos-option.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/nixos-option.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nixos-option

NixOS 설정을 확인합니다.
더 많은 정보: <https://nixos.org/manual/nixos/stable/index.html#sec-modularity>.

- 주어진 옵션 키의 모든 하위 키 나열:

`nixos-option `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">옵션_키</span>

- 현재 부팅 커널 모듈 나열:

`nixos-option boot.kernelModules`

- 특정 사용자의 인증된 키 나열:

`nixos-option users.users.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>`.openssh.authorizedKeys.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_파일|키</span>

- 모든 원격 빌더 나열:

`nixos-option nix.buildMachines`

- 다른 NixOS 설정에서 주어진 키의 모든 하위 키 나열:

`NIXOS_CONFIG=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/configuration.nix</span>` nixos-option `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">옵션_키</span>

- 사용자의 모든 값을 재귀적으로 표시:

`nixos-option -r users.users.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>
