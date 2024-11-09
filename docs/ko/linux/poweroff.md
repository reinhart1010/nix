---
layout: page
title: linux/poweroff (한국어)
description: "시스템을 종료합니다."
content_hash: 2c6096d0621e6847c025cfc489100d2633d3aad5
last_modified_at: 2024-11-09
related_topics:
  - title: català version
    url: /ca/linux/poweroff.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/poweroff.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/poweroff.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/poweroff.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/poweroff.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/poweroff.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/poweroff.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/poweroff.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># poweroff

시스템을 종료합니다.
더 많은 정보: <https://www.manned.org/poweroff>.

- 시스템 종료:

`poweroff`

- 시스템 정지 (`halt`와 동일):

`poweroff --halt`

- 시스템 재부팅 (`reboot`와 동일):

`poweroff --reboot`

- 시스템 관리자에게 알리지 않고 즉시 종료:

`poweroff --force`

- 시스템을 종료하지 않고 wtmp 종료 항목 작성:

`poweroff --wtmp-only`
