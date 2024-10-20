---
layout: page
title: common/fc-cache (한국어)
description: "글꼴 디렉터리를 스캔하여 글꼴 캐시 파일을 만듬."
content_hash: c5e87371c758007a67ab659176ca2157fcbdd6d9
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/fc-cache.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/fc-cache.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/fc-cache.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fc-cache

글꼴 디렉터리를 스캔하여 글꼴 캐시 파일을 만듬.
더 많은 정보: <https://manned.org/fc-cache>.

- 글꼴 캐시 파일 생성:

`fc-cache`

- 캐시가 최신인지 확인하지 않고, 모든 글꼴 캐시 파일을 강제로 다시 빌드:

`fc-cache -f`

- 글꼴 캐시 파일을 지우고, 새 글꼴 캐시 파일을 생성:

`fc-cache -r`
