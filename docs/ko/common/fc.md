---
layout: page
title: common/fc (한국어)
description: "편집할 최신 명령을 열고 실행."
content_hash: eb9c472305d76d1d7f14b1d8eb7cc143fd6a5f95
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/fc.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/fc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/fc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/fc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/fc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fc

편집할 최신 명령을 열고 실행.
더 많은 정보: <https://manned.org/fc>.

- 기본 시스템 편집기에서 마지막 명령을 열고 편집 후 실행:

`fc`

- 열 때 사용할 편집기를 지정:

`fc -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'emacs'</span>

- 기록에서 최근 명령을 나열:

`fc -l`

- 최근 명령을 역순을 나열:

`fc -l -r`

- 기록에서 명령을 편집하고 실행:

`fc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">숫자</span>

- 주어진 간격으로 명령을 편집하고 실행함:

`fc '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">416</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">420</span>`'`

- 도움말 표시:

`fc --help`
