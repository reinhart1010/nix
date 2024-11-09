---
layout: page
title: linux/timedatectl (한국어)
description: "시스템 시간과 날짜를 제어합니다."
content_hash: baab7ac2c80d211485929c725a104a0657d82002
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/timedatectl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/timedatectl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/timedatectl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/timedatectl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># timedatectl

시스템 시간과 날짜를 제어합니다.
더 많은 정보: <https://manned.org/timedatectl>.

- 현재 시스템 시계 시간 확인:

`timedatectl`

- 시스템 시계의 로컬 시간을 직접 설정:

`timedatectl set-time "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yyyy-MM-dd hh:mm:ss</span>`"`

- 사용 가능한 시간대 나열:

`timedatectl list-timezones`

- 시스템 시간대 설정:

`timedatectl set-timezone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시간대</span>

- 네트워크 시간 프로토콜(NTP) 동기화 활성화:

`timedatectl set-ntp on`

- 하드웨어 시계 시간 기준을 로컬 시간으로 변경:

`timedatectl set-local-rtc 1`
