---
layout: page
title: common/nix-build (한국어)
description: "Nix 표현식을 빌드."
content_hash: 894c87429dde1fd0f836977c5ab2f76fbbf21394
last_modified_at: 2024-11-02
related_topics:
  - title: Deutsch version
    url: /de/common/nix-build.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/nix-build.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nix-build

Nix 표현식을 빌드.
같이 보기: `nix3 build`.
더 많은 정보: <https://nixos.org/manual/nix/stable/command-ref/nix-build.html>.

- Nix 표현식 빌드:

`nix-build '<nixpkgs>' --attr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firefox</span>

- 샌드박스된 Nix 표현식 빌드 (NixOS가 아닌 경우):

`nix-build '<nixpkgs>' --attr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firefox</span>` --option sandbox true`
