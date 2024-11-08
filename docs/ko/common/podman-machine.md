---
layout: page
title: common/podman-machine (한국어)
description: "Podman을 실행하는 가상 머신을 생성하고 관리."
content_hash: c6c04c300b237e7b4fdf31c7cac3ee3f626b1184
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/podman-machine.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/podman-machine.html
    icon: bi bi-globe
tldri18n_status: 2
---
# podman machine

Podman을 실행하는 가상 머신을 생성하고 관리.
Podman 버전 4 이상에 포함되어 있습니다.
더 많은 정보: <https://docs.podman.io/en/latest/markdown/podman-machine.1.html>.

- 기존 머신 나열:

`podman machine ls`

- 기본 머신 생성:

`podman machine init`

- 특정 이름의 새 머신 생성:

`podman machine init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 다른 리소스로 새 머신 생성:

`podman machine init --cpus=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` --memory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4096</span>` --disk-size=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>

- 머신 시작 또는 중지:

`podman machine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- SSH를 통해 실행 중인 머신에 연결:

`podman machine ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 머신 정보 검사:

`podman machine inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>
