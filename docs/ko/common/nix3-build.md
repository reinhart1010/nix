---
layout: page
title: common/nix3-build (한국어)
description: "Nix 표현식을 빌드합니다 (가능할 경우 캐시에서 다운로드)."
content_hash: 7ccf35cf72d36bf92410c2094a59c33fc9843f20
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/nix3-build.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nix build

Nix 표현식을 빌드합니다 (가능할 경우 캐시에서 다운로드).
같이 보기: 전통적인 Nix 표현식 빌드에 대한 `nix-build`, flakes에 대한 정보는 `nix3 flake`.
더 많은 정보: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-build.html>.

- nixpkgs에서 패키지를 빌드하고 결과를 `./result`에 심볼릭 링크:

`nix build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs#pkg</span>

- 현재 디렉토리의 flake에서 패키지를 빌드하고 빌드 로그를 표시:

`nix build -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.#pkg</span>

- 특정 디렉토리의 flake에서 기본 패키지 빌드:

`nix build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./경로/대상/폴더</span>

- `result` 심볼릭 링크를 생성하지 않고 패키지를 빌드하며 대신 저장소 경로를 `stdout`에 출력:

`nix build --no-link --print-out-paths`
