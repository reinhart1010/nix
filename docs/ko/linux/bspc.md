---
layout: page
title: linux/bspc (한국어)
description: "`bspwm`을 구성하고 제어하여 노드, 데스크톱, 모니터 등을 관리합니다."
content_hash: e312a442d8d6b8ea196fb045306d7a1e43b7d1c3
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/bspc.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/bspc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/bspc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bspc

`bspwm`을 구성하고 제어하여 노드, 데스크톱, 모니터 등을 관리합니다.
같이 보기: `bspwm`.
더 많은 정보: <https://github.com/baskerville/bspwm>.

- 두 개의 가상 데스크톱 정의:

`bspc monitor --reset-desktops `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데스크톱_이름1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데스크톱_이름2</span>

- 지정한 데스크톱으로 포커스 이동:

`bspc desktop --focus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">번호</span>

- 선택한 노드에 있는 창 닫기:

`bspc node --close`

- 선택한 노드를 지정한 데스크톱으로 보내기:

`bspc node --to-desktop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">번호</span>

- 선택한 노드의 전체 화면 모드 전환:

`bspc node --state ~fullscreen`

- 특정 설정의 값 설정:

`bspc config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">설정_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>
