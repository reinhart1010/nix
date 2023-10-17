---
layout: page
title: linux/systemctl (한국어)
description: "systemd 시스템 및 서비스 관리자를 제어합니다."
content_hash: 55a1802e1e84eaf864d0d36373bb1a453568b73e
last_modified_at: 2023-10-17
related_topics:
  - title: català version
    url: /ca/linux/systemctl.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/systemctl.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/systemctl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/systemctl.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/systemctl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/systemctl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/systemctl.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># systemctl

systemd 시스템 및 서비스 관리자를 제어합니다.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemctl.html>.

- 실행 중인 서비스 모두 표시:

`systemctl status`

- 실패한 장치를 나열:

`systemctl --failed`

- 서비스 시작/중지/다시 시작/다시 로드:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop|restart|reload</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치</span>

- 장치 상태 표시:

`systemctl status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치</span>

- 부팅 시 시작될 장치를 활성화/비활성화:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enable|disable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치</span>

- 자동 및 수동 활성화를 방지하기 위해 장치 마스크/마스크 해제:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mask|unmask</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치</span>

- systemd를 다시 로드하고, 새 장치 또는 변경된 장치를 검색:

`systemctl daemon-reload`

- 장치가 활성화되어 있는지 확인:

`systemctl is-enabled `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치</span>
