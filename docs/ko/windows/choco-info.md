---
layout: page
title: windows/choco-info (한국어)
description: "Chocolatey를 사용하여 패키지에 대한 자세한 정보 표시."
content_hash: f4dbb218612fb7fefeb3f7cfd0064d1cb4e90a85
last_modified_at: 2024-10-14
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-info.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-info.html
    icon: bi bi-globe
  - title: français version
    url: /fr/windows/choco-info.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/choco-info.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-info.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-info.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-info.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-info.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/choco-info.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># choco info

Chocolatey를 사용하여 패키지에 대한 자세한 정보 표시.
더 많은 정보: <https://chocolatey.org/docs/commands-info>.

- 특정 패키지에 대한 정보 표시:

`choco info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 로컬 패키지에 대한 정보만 표시:

`choco info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` --local-only`

- 패키지 정보를 받을 사용자 지정 소스 지정:

`choco info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_url|별칭</span>

- 인증을 위한 사용자 명과 비밀번호 제공:

`choco info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>
