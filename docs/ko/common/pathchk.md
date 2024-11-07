---
layout: page
title: common/pathchk (한국어)
description: "경로명의 유효성과 이식성을 확인합니다."
content_hash: e57d4bb1604b0b2aad1d41c8aa1bdd402bbabfc7
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pathchk.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pathchk.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/pathchk.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pathchk.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pathchk

경로명의 유효성과 이식성을 확인합니다.
더 많은 정보: <https://www.gnu.org/software/coreutils/pathchk>.

- 현재 시스템에서 경로명의 유효성을 확인:

`pathchk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로1 경로2 …</span>

- 더 넓은 범위의 POSIX 호환 시스템에서 경로명의 유효성을 확인:

`pathchk -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로1 경로2 …</span>

- 모든 POSIX 호환 시스템에서 경로명의 유효성을 확인:

`pathchk --portability `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로1 경로2 …</span>

- 빈 경로나 선행 대시(-)만 확인:

`pathchk -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로1 경로2 …</span>
