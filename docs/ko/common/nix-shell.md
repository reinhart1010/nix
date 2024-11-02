---
layout: page
title: common/nix-shell (한국어)
description: "Nix 표현을 기반으로 대화형 셸 시작."
content_hash: 16837de74ed862041f7d1bc974af6fe903f33191
last_modified_at: 2024-11-02
related_topics:
  - title: Deutsch version
    url: /de/common/nix-shell.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/nix-shell.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nix-shell

Nix 표현을 기반으로 대화형 셸 시작.
같이 보기: `nix3 shell`.
더 많은 정보: <https://nixos.org/manual/nix/stable/command-ref/nix-shell.html>.

- 현재 디렉터리의 `shell.nix` 또는 `default.nix`의 nix 표현으로 시작:

`nix-shell`

- 비대화형 셸에서 셸 명령 실행 후 종료:

`nix-shell --run "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수1 인수2 ...</span>`"`

- 현재 디렉터리의 `default.nix`의 표현으로 시작:

`nix-shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">default.nix</span>

- nixpkgs에서 로드된 패키지로 시작:

`nix-shell --packages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지1 패키지2 ...</span>

- 특정 nixpkgs 리비전에서 로드된 패키지로 시작:

`nix-shell --packages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지1 패키지2 ...</span>` -I nixpkgs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://github.com/NixOS/nixpkgs/archive/nixpkgs_revision.tar.gz</span>

- 특정 인터프리터에서 파일의 나머지를 평가하여 `#!-scripts`에서 사용 (자세한 내용은 <https://nixos.org/manual/nix/stable/#use-as-a-interpreter> 참고):

`nix-shell -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터프리터</span>` --packages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지1 패키지2 ...</span>
