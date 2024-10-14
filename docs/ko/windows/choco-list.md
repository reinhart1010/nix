---
layout: page
title: windows/choco-list (한국어)
description: "Chocolatey로 패키지 목록 표시."
content_hash: 39557b6966dafb24c9ccd2d56404318a2c92e45f
last_modified_at: 2024-10-14
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-list.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-list.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/choco-list.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-list.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-list.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-list.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-list.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/choco-list.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># choco list

Chocolatey로 패키지 목록 표시.
더 많은 정보: <https://chocolatey.org/docs/commands-list>.

- 사용 가능한 모든 패키지 표시:

`choco list`

- 로컬에 설치된 모든 패키지 표시:

`choco list --local-only`

- 로컬 프로그램을 포함한 목록 표시:

`choco list --include-programs`

- 승인된 패키지만 표시:

`choco list --approved-only`

- 사용자 정의 소스를 지정하여 패키지 표시:

`choco list --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스_url|별칭</span>

- 인증을 위한 사용자 명과 비밀번호 제공:

`choco list --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>
