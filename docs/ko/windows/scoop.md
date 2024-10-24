---
layout: page
title: windows/scoop (한국어)
description: "Scoop 패키지 관리자."
content_hash: 98a948156f5ff70c6ed18b663278f7d99d0b1545
last_modified_at: 2024-10-24
related_topics:
  - title: বাংলা version
    url: /bn/windows/scoop.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/windows/scoop.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/scoop.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/scoop.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/scoop.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/scoop.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/scoop.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># scoop

Scoop 패키지 관리자.
`bucket`과 같은 하위 명령어는 자체 문서를 가지고 있습니다.
더 많은 정보: <https://scoop.sh>.

- 패키지 설치:

`scoop install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 제거:

`scoop uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 모든 설치된 패키지 업데이트:

`scoop update --all`

- 설치된 패키지 목록 표시:

`scoop list`

- 패키지 정보 표시:

`scoop info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 검색:

`scoop search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 모든 패키지의 이전 버전 제거 및 다운로드 캐시 정리:

`scoop cleanup --cache --all`
