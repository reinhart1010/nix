---
layout: page
title: linux/rc-update (한국어)
description: "OpenRC 서비스를 실행 수준에 추가 및 제거."
content_hash: e740170a2f1d6a725d8e36206c173fc684495f95
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/rc-update.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rc-update

OpenRC 서비스를 실행 수준에 추가 및 제거.
같이 보기: `openrc`.
더 많은 정보: <https://manned.org/rc-update>.

- 모든 서비스와 추가된 실행 수준 나열:

`rc-update show`

- 서비스를 실행 수준에 추가:

`sudo rc-update add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">실행_수준</span>

- 실행 수준에서 서비스 제거:

`sudo rc-update delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">실행_수준</span>

- 모든 실행 수준에서 서비스 제거:

`sudo rc-update --all delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름</span>
