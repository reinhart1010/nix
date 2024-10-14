---
layout: page
title: windows/choco-pin (한국어)
description: "Chocolatey로 특정 버전의 패키지를 고정."
content_hash: 6b7abe97e198c2bf18d0e4b4562b92f745778168
last_modified_at: 2024-10-14
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-pin.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-pin.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-pin.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-pin.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-pin.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/choco-pin.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># choco pin

Chocolatey로 특정 버전의 패키지를 고정.
고정된 패키지는 업그레이드 시 자동으로 건너뜁니다.
더 많은 정보: <https://chocolatey.org/docs/commands-pin>.

- 고정된 패키지 및 해당 버전을 나열:

`choco pin list`

- 현재 버전으로 패키지를 고정:

`choco pin add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 특정 버전으로 패키지를 고정:

`choco pin add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 특정 패키지에 대한 고정을 제거:

`choco pin remove --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>
