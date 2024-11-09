---
layout: page
title: linux/halt (한국어)
description: "시스템을 중지합니다."
content_hash: 0b5db56ee499ceff11dab42ee54768547421226d
last_modified_at: 2024-11-09
related_topics:
  - title: català version
    url: /ca/linux/halt.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/halt.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/halt.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/halt.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/halt.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/halt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># halt

시스템을 중지합니다.
더 많은 정보: <https://manned.org/halt.8>.

- 시스템 중지:

`halt`

- 시스템 전원 끄기 (`poweroff`와 동일):

`halt --poweroff`

- 시스템 재부팅 (`reboot`와 동일):

`halt --reboot`

- 시스템 관리자와 상의하지 않고 즉시 중지:

`halt --force`

- 시스템을 중지하지 않고 wtmp 종료 항목 작성:

`halt --wtmp-only`
