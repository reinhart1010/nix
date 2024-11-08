---
layout: page
title: linux/dysk (한국어)
description: "파일 시스템 정보를 표 형식으로 표시합니다."
content_hash: c742e1532a5986d131b11ca7b8764559ae678229
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/dysk.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dysk.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dysk.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dysk

파일 시스템 정보를 표 형식으로 표시합니다.
더 많은 정보: <https://dystroy.org/dysk>.

- 일반 디스크에 대한 표준 개요 확인:

`dysk`

- 여유 크기로 정렬:

`dysk --sort free`

- HDD 디스크만 포함:

`dysk --filter 'disk = HDD'`

- SSD 디스크 제외:

`dysk --filter 'disk <> SSD'`

- 높은 사용률 또는 낮은 여유 공간을 가진 디스크 표시:

`dysk --filter 'use > 65% | free < 50G'`
