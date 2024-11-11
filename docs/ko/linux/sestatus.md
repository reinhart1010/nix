---
layout: page
title: linux/sestatus (한국어)
description: "현재 SELinux 상태를 표시합니다."
content_hash: a05cf8bd0af8fd55280bb1956ed6d0ccdcceee84
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/sestatus.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/sestatus.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sestatus

현재 SELinux 상태를 표시합니다.
더 많은 정보: <https://manned.org/sestatus>.

- 현재 상태 표시:

`sestatus`

- 모든 정책 불리언의 현재 상태 표시:

`sestatus -b`

- 현재 파일 및 프로세스 컨텍스트 표시:

`sestatus -v`
