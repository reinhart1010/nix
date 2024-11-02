---
layout: page
title: common/nix3-flake (한국어)
description: "Nix 플레이크 관리."
content_hash: fe88067327e608f9f80db423895a64a62d62b18d
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/nix3-flake.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nix flake

Nix 플레이크 관리.
더 많은 정보: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-flake.html>.

- 현재 디렉토리에서 기본 템플릿으로 새로운 플레이크(`flake.nix` 파일만) 생성:

`nix flake init`

- 현재 디렉토리의 플레이크의 모든 입력(의존성) 업데이트:

`nix flake update`

- 현재 디렉토리의 플레이크의 특정 입력(의존성) 업데이트:

`nix flake lock --update-input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력</span>

- GitHub에 있는 플레이크의 모든 출력 표시:

`nix flake show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">github:소유자/레포</span>

- 도움말 표시:

`nix flake --help`
