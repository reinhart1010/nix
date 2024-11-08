---
layout: page
title: linux/atop (한국어)
description: "Linux 시스템 및 프로세스 모니터."
content_hash: 9159bf2025325d1e4de9ee0507ef1ac41dc3e01c
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/atop.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/atop.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># atop

Linux 시스템 및 프로세스 모니터.
더 많은 정보: <https://manned.org/atop>.

- 시작:

`atop`

- 시작하고 각 프로세스의 메모리 소비량 표시:

`atop -m`

- 시작하고 디스크 정보 표시:

`atop -d`

- 시작하고 백그라운드 프로세스 정보 표시:

`atop -c`

- 시작하고 스레드별 자원 사용 정보 표시:

`atop -y`

- 시작하고 각 사용자별 프로세스 수 표시:

`atop -au`

- 인터랙티브 명령에 대한 도움말 표시:

`?`
