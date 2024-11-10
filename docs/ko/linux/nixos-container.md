---
layout: page
title: linux/nixos-container (한국어)
description: "Linux 컨테이너를 사용하여 NixOS 컨테이너 시작."
content_hash: a13a977dc189765a9b00834b5ccff1a34d79bc5e
last_modified_at: 2024-11-10
related_topics:
  - title: Deutsch version
    url: /de/linux/nixos-container.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/nixos-container.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nixos-container

Linux 컨테이너를 사용하여 NixOS 컨테이너 시작.
더 많은 정보: <https://nixos.org/manual/nixos/stable/#ch-containers>.

- 실행 중인 컨테이너 나열:

`sudo nixos-container list`

- 특정 구성 파일로 NixOS 컨테이너 생성:

`sudo nixos-container create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>` --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nix_구성_파일_경로</span>

- 특정 컨테이너 시작, 중지, 종료, 또는 삭제:

`sudo nixos-container `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop|terminate|destroy|status</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>

- 실행 중인 컨테이너에서 명령어 실행:

`sudo nixos-container run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어_인자들</span>

- 컨테이너 구성 업데이트:

`sudo $EDITOR /var/lib/container/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>`/etc/nixos/configuration.nix && sudo nixos-container update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>

- 이미 실행 중인 컨테이너에 대한 대화형 셸 세션 시작:

`sudo nixos-container root-login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>
