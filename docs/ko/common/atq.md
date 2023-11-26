---
layout: page
title: common/atq (한국어)
description: "`at` 또는 `batch` 명령으로 예약된 작업 표시."
content_hash: 2ba0bf5fa3c9f882625a3e60bbd5f3c8db2176c0
last_modified_at: 2023-11-26
related_topics:
  - title: English version
    url: /en/common/atq.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/atq.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/atq.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/atq.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/atq.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># atq

`at` 또는 `batch` 명령으로 예약된 작업 표시.
더 많은 정보: <https://manned.org/atq>.

- 현재 사용자의 예약된 작업 표시:

`atq`

- 'a'라는 대기열의 작업 표시 (대기열에는 단일 문자 이름이 있음):

`atq -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a</span>

- 모든 사용자의 직업 표시 (슈퍼유저로 실행):

`sudo atq`
