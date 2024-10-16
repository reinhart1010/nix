---
layout: page
title: windows/tree (한국어)
description: "경로의 디렉토리 구조에 대한 그래픽 트리를 표시합니다."
content_hash: 7d8f666064f2756ffa305fe875cd4b3fcfac2588
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/windows/tree.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/tree.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/tree.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/tree.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/tree.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/tree.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/tree.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tree

경로의 디렉토리 구조에 대한 그래픽 트리를 표시합니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/tree>.

- 현재 디렉토리에 대한 트리 표시:

`tree`

- 특정 디렉토리에 대한 트리 표시:

`tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\폴더</span>

- 특정 디렉토리에 대한 트리 표시 (파일 포함):

`tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\폴더</span>` /f`

- 트리 표시 그래픽 문자 대신 ASCII 문자 사용:

`tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\폴더</span>` /a`
