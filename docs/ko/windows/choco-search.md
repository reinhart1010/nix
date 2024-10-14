---
layout: page
title: windows/choco-search (한국어)
description: "Chocolatey로 로컬 또는 원격 패키지를 검색."
content_hash: 7356dace1b01bed637cee48169c11237b862a474
last_modified_at: 2024-10-14
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-search.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-search.html
    icon: bi bi-globe
  - title: français version
    url: /fr/windows/choco-search.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-search.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-search.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-search.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/choco-search.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># choco search

Chocolatey로 로컬 또는 원격 패키지를 검색.
더 많은 정보: <https://chocolatey.org/docs/commands-search>.

- 패키지 검색:

`choco search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쿼리</span>

- 로컬에서 패키지 검색:

`choco search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쿼리</span>` --local-only`

- 결과에서 정확히 일치하는 항목만 포함:

`choco search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쿼리</span>` --exact`

- 모든 프롬프트를 자동으로 확인:

`choco search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쿼리</span>` --yes`

- 패키지 검색을 위한 사용자 지정 소스 지정:

`choco search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쿼리</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스_url|별칭</span>

- 인증을 위한 사용자 명과 비밀번호 제공:

`choco search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쿼리</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>
