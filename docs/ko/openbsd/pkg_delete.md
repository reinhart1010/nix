---
layout: page
title: openbsd/pkg_delete (한국어)
description: "OpenBSD에서 패키지를 제거합니다."
content_hash: 4c1ff00317ac642aafe7502ba2cd65cc4a8c2f59
last_modified_at: 2024-06-23
related_topics:
  - title: English version
    url: /en/openbsd/pkg_delete.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/openbsd/pkg_delete.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/openbsd/pkg_delete.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/openbsd/pkg_delete.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/openbsd/pkg_delete.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pkg_delete

OpenBSD에서 패키지를 제거합니다.
같이 보기: `pkg_add`, `pkg_info`.
더 많은 정보: <https://man.openbsd.org/pkg_delete>.

- 패키지 삭제:

`pkg_delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 사용되지 않는 의존성을 포함하여 패키지 삭제:

`pkg_delete -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지의 Dry-run 삭제:

`pkg_delete -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>
