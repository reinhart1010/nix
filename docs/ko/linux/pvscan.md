---
layout: page
title: linux/pvscan (한국어)
description: "모든 물리적 볼륨을 나열하고 온라인 상태를 관리합니다."
content_hash: 74a9ac770415dfb7d1ce4a25858e749f8a487a7f
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/pvscan.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pvscan

모든 물리적 볼륨을 나열하고 온라인 상태를 관리합니다.
더 많은 정보: <https://manned.org/pvscan>.

- 모든 물리적 볼륨 나열:

`pvscan`

- 특정 물리적 볼륨을 사용하는 볼륨 그룹 표시:

`pvscan --cache --listvg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- 특정 물리적 볼륨을 사용하는 논리 볼륨 표시:

`pvscan --cache --listlvs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- JSON 형식으로 자세한 정보 표시:

`pvscan --reportformat json`
