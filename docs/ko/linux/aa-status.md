---
layout: page
title: linux/aa-status (한국어)
description: "현재 로드된 AppArmor 모듈 나열."
content_hash: 316624ddcedaa493c11c5d9264f0aedf375f2a6d
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/aa-status.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/aa-status.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/aa-status.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/aa-status.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/aa-status.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aa-status

현재 로드된 AppArmor 모듈 나열.
같이 보기: `aa-complain`, `aa-disable`, `aa-enforce`.
더 많은 정보: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-status.8>.

- 상태 확인:

`sudo aa-status`

- 로드된 정책의 수 표시:

`sudo aa-status --profiled`

- 로드된 시행 정책의 수 표시:

`sudo aa-status --enforced`

- 로드된 비시행 정책의 수 표시:

`sudo aa-status --complaining`

- 작업을 종료하는 로드된 시행 정책의 수 표시:

`sudo aa-status --kill`
