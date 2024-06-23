---
layout: page
title: openbsd/pkg_info (한국어)
description: "OpenBSD의 패키지에 대한 정보를 확인합니다."
content_hash: 1db8f67c15411d85daef1260dc47adb11ac93694
last_modified_at: 2024-06-23
related_topics:
  - title: English version
    url: /en/openbsd/pkg_info.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/openbsd/pkg_info.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/openbsd/pkg_info.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/openbsd/pkg_info.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/openbsd/pkg_info.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pkg_info

OpenBSD의 패키지에 대한 정보를 확인합니다.
같이 보기: `pkg_add`, `pkg_delete`.
더 많은 정보: <https://man.openbsd.org/pkg_info>.

- 패키지 이름을 사용해 패키지 검색:

`pkg_info -Q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- `pkg_add -l`과 함께 사용할 설치된 패키지 목록을 출력:

`pkg_info -mz`
