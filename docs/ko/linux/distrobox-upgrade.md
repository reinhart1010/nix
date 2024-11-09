---
layout: page
title: linux/distrobox-upgrade (한국어)
description: "하나 또는 여러 Distrobox 컨테이너를 업그레이드합니다. 같이 보기: `tldr distrobox`."
content_hash: c39b3e56656799b63dc4cc5d391226582d37b835
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/distrobox-upgrade.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/distrobox-upgrade.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/distrobox-upgrade.html
    icon: bi bi-globe
tldri18n_status: 2
---
# distrobox-upgrade

하나 또는 여러 Distrobox 컨테이너를 업그레이드합니다. 같이 보기: `tldr distrobox`.
더 많은 정보: <https://distrobox.it/usage/distrobox-upgrade>.

- 컨테이너의 기본 패키지 관리자를 사용하여 컨테이너 업그레이드:

`distrobox-upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>

- 모든 컨테이너를 기본 패키지 관리자를 사용하여 업그레이드:

`distrobox-upgrade --all`

- 특정 컨테이너를 기본 패키지 관리자를 통해 업그레이드:

`distrobox-upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너1 컨테이너2 ...</span>
