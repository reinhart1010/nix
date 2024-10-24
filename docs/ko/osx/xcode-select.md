---
layout: page
title: osx/xcode-select (한국어)
description: "Xcode의 다양한 버전과 포함된 개발자 도구 간에 전환."
content_hash: b0feaecee56d7c6805747edb7c37fb823a61cd30
last_modified_at: 2024-10-24
related_topics:
  - title: Deutsch version
    url: /de/osx/xcode-select.html
    icon: bi bi-globe
  - title: English version
    url: /en/osx/xcode-select.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/xcode-select.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/osx/xcode-select.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xcode-select

Xcode의 다양한 버전과 포함된 개발자 도구 간에 전환.
설치 후 Xcode가 이동된 경우 경로를 업데이트하는 데 사용됩니다.
더 많은 정보: <https://developer.apple.com/library/archive/technotes/tn2339/_index.html>.

- Xcode의 명령줄 도구 설치:

`xcode-select --install`

- 주어진 경로를 활성 개발자 디렉토리로 선택:

`xcode-select --switch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/Xcode.app/Contents/Developer</span>

- 주어진 Xcode 인스턴스를 선택하고 해당 개발자 디렉토리를 활성 디렉토리로 사용:

`xcode-select --switch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/Xcode_파일.app</span>

- 현재 선택된 개발자 디렉토리 출력:

`xcode-select --print-path`

- 사용자 지정 개발자 디렉토리를 삭제하여 기본 검색 메커니즘을 통해 찾도록 설정:

`sudo xcode-select --reset`
