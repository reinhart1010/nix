---
layout: page
title: linux/smem (한국어)
description: "프로그램의 메모리 사용량을 표시합니다."
content_hash: cf0ddf44127e797a2afedf3bfef541f9d21e6629
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/smem.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/smem.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># smem

프로그램의 메모리 사용량을 표시합니다.
더 많은 정보: <https://manned.org/smem>.

- 현재 프로세스의 메모리 사용량 표시:

`smem`

- 시스템의 모든 사용자의 현재 프로세스 메모리 사용량 표시:

`smem --users`

- 지정된 사용자의 현재 프로세스 메모리 사용량 표시:

`smem --userfilter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 시스템 메모리 정보 표시:

`smem --system`
