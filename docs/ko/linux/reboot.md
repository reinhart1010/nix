---
layout: page
title: linux/reboot (한국어)
description: "시스템을 재부팅합니다."
content_hash: 81fba1f3a9950cbc79e42d0635cb23cde18bc874
last_modified_at: 2024-11-10
related_topics:
  - title: català version
    url: /ca/linux/reboot.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/reboot.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/reboot.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/reboot.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/reboot.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/reboot.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/reboot.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/reboot.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/reboot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# reboot

시스템을 재부팅합니다.
더 많은 정보: <https://manned.org/reboot.8>.

- 시스템 재부팅:

`reboot`

- 시스템 전원 끄기 (`poweroff`와 동일):

`reboot --poweroff`

- 시스템 중지 (모든 프로세스를 종료하고 CPU를 셧다운) (`halt`와 동일):

`reboot --halt`

- 시스템 관리자를 거치지 않고 즉시 재부팅:

`reboot --force`

- 시스템을 재부팅하지 않고 wtmp 종료 항목 기록:

`reboot --wtmp-only`
