---
layout: page
title: linux/cacaclock (한국어)
description: "현재 시간을 ASCII 아트로 표시합니다."
content_hash: de904f78914a16f4c2288ba04e4853617f27291e
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/cacaclock.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/cacaclock.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/cacaclock.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cacaclock

현재 시간을 ASCII 아트로 표시합니다.
더 많은 정보: <https://packages.debian.org/sid/caca-utils>.

- 시간 표시:

`cacaclock`

- 글꼴 변경:

`cacaclock -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">글꼴</span>

- `strftime` 형식 사양을 사용하여 형식 변경:

`cacaclock -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">strftime_인수</span>
