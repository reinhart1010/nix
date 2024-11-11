---
layout: page
title: linux/systemctl (한국어)
description: "systemd 시스템 및 서비스 관리자를 제어합니다."
content_hash: ecda6a8cc9d09be49359ec9cabc50a0ffa7f5a65
last_modified_at: 2024-11-11
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
  - title: українська version
    url: /uk/linux/systemctl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/systemctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# systemctl

systemd 시스템 및 서비스 관리자를 제어합니다.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemctl.html>.

- 실행 중인 서비스 모두 표시:

`systemctl status`

- 실패한 유닛 나열:

`systemctl --failed`

- 서비스 시작/중지/재시작/재로드/상태 표시:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop|restart|reload|status</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">유닛</span>

- 부팅 시 시작할 유닛 활성화/비활성화:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enable|disable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">유닛</span>

- systemd를 재로드하고 새 유닛 또는 변경된 유닛 검색:

`systemctl daemon-reload`

- 유닛이 활성/활성화됨/실패했는지 확인:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">is-active|is-enabled|is-failed</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">유닛</span>

- 실행 중이거나 실패한 상태로 필터링하여 모든 서비스/소켓/자동 마운트 유닛 나열:

`systemctl list-units --type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service|socket|automount</span>` --state=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">failed|running</span>

- 유닛 파일의 내용 및 절대 경로 표시:

`systemctl cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">유닛</span>
