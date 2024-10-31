---
layout: page
title: windows/path (한국어)
description: "실행 파일에 대한 검색 경로를 표시하거나 설정합니다."
content_hash: 4bf362f66fe0786fbf21d3b04157bf2455daa40c
last_modified_at: 2024-10-31
related_topics:
  - title: বাংলা version
    url: /bn/windows/path.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/path.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/path.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/path.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/path.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/path.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># path

실행 파일에 대한 검색 경로를 표시하거나 설정합니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/path>.

- 현재 경로 표시:

`path`

- 세미콜론으로 구분된 하나 이상의 디렉토리로 경로 설정:

`path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\디렉토리1 경로\대상\디렉토리2 ...</span>

- 원래 경로에 새 디렉토리 추가:

`path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\디렉토리</span>`;%path%`

- 실행 파일을 현재 디렉토리에서만 검색하도록 명령 프롬프트를 설정:

`path ;`
