---
layout: page
title: common/nix3-why-depends (한국어)
description: "패키지가 다른 패키지에 의존하는 이유를 보여줍니다."
content_hash: 4aed297c02eec148ced48990fa1c0c0ab340affc
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/nix3-why-depends.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nix why-depends

패키지가 다른 패키지에 의존하는 이유를 보여줍니다.
더 많은 정보: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-why-depends.html>.

- 현재 실행 중인 NixOS 시스템이 특정 저장소 경로를 요구하는 이유를 표시:

`nix why-depends `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/run/현재_시스템</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/nix/store/...</span>

- nixpkgs의 패키지가 다른 패키지를 _빌드 타임_ 의존성으로 요구하는 이유를 표시:

`nix why-depends --derivation `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs#의존자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs#의존성</span>
