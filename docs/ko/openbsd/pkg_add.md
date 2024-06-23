---
layout: page
title: openbsd/pkg_add (한국어)
description: "OpenBSD에 패키지를 설치/업데이트합니다."
content_hash: 6bfa7c152c63e60b923f36e95d7118fdd6dc03df
last_modified_at: 2024-06-23
related_topics:
  - title: English version
    url: /en/openbsd/pkg_add.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/openbsd/pkg_add.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/openbsd/pkg_add.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/openbsd/pkg_add.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/openbsd/pkg_add.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pkg_add

OpenBSD에 패키지를 설치/업데이트합니다.
같이 보기: `pkg_info`, `pkg_delete`.
더 많은 정보: <https://man.openbsd.org/pkg_add>.

- 종속성을 포함하여 모든 패키지를 업데이트:

`pkg_add -u`

- 새로운 패키지 설치:

`pkg_add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- `pkg_info`의 원시 출력에서 패키지 설치:

`pkg_add -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
