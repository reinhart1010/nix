---
layout: page
title: linux/envycontrol (한국어)
description: "Nvidia Optimus 노트북을 위한 GPU 전환 도구."
content_hash: f73aa8244fd337495314715cfb0f744160b312f8
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/envycontrol.html
    icon: bi bi-globe
tldri18n_status: 2
---
# envycontrol

Nvidia Optimus 노트북을 위한 GPU 전환 도구.
더 많은 정보: <https://github.com/bayasdev/envycontrol>.

- 다른 GPU 모드로 전환:

`sudo envycontrol -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nvidia|integrated|hybrid</span>

- 디스플레이 관리자 수동 지정:

`envycontrol --dm`

- 현재 GPU 모드 확인:

`sudo envycontrol --query`

- 설정 초기화:

`sudo envycontrol --reset`

- 도움말 표시:

`envycontrol --help`

- 버전 표시:

`envycontrol --version`
