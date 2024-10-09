---
layout: page
title: windows/winget (한국어)
description: "윈도우 패키지 매니저."
content_hash: 7b5bd92e25f77e6a4fd92a91ee869f28f1ce0ea7
last_modified_at: 2024-10-09
related_topics:
  - title: Deutsch version
    url: /de/windows/winget.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/winget.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/winget.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/winget.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/winget.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/winget.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/winget.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/winget.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/winget.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># winget

윈도우 패키지 매니저.
더 많은 정보: <https://learn.microsoft.com/windows/package-manager/winget>.

- 패키지 설치:

`winget install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 제거 (참고: `remove` 대신 `uninstall` 을 사용할 수 있음):

`winget uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지에 대한 정보 표시:

`winget show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 검색:

`winget search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 모든 패키지를 최신 버전으로 업그레이드:

`winget upgrade --all`

- 관리할 수 있는 모든 패키지 나열:

`winget list --source winget`

- 파일에서 패키지 가져오기 또는 설치된 패키지를 파일로 내보내기:

`winget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import|export</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--import-file|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- winget 매니페스트 패키지 저장소에 PR을 제출하기 전에 유효성 검사:

`winget validate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/매니페스트</span>
