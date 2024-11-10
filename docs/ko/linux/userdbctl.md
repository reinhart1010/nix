---
layout: page
title: linux/userdbctl (한국어)
description: "시스템의 사용자, 그룹 및 그룹 멤버십을 검사합니다."
content_hash: cf42de0e5853874a5a8b5725b26353fdb658b97e
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/userdbctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# userdbctl

시스템의 사용자, 그룹 및 그룹 멤버십을 검사합니다.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/userdbctl.html>.

- 모든 알려진 사용자 기록 나열:

`userdbctl user`

- 특정 사용자 세부 정보 표시:

`userdbctl user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 모든 알려진 그룹 나열:

`userdbctl group`

- 특정 그룹 세부 정보 표시:

`userdbctl group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹명</span>

- 현재 시스템에 사용자/그룹 정의를 제공하는 모든 서비스 나열:

`userdbctl services`
