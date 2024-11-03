---
layout: page
title: windows/get-history (한국어)
description: "PowerShell 명령 히스토리 표시."
content_hash: 80b20e4084632621e8b80b6fc48a8d677d3c965b
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/windows/get-history.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/get-history.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Get-History

PowerShell 명령 히스토리 표시.
참고: 이 명령은 PowerShell을 통해서만 사용할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/get-history>.

- ID와 함께 명령 히스토리 목록 표시:

`Get-History`

- ID로 PowerShell 히스토리 항목 가져오기:

`Get-History -Id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- 마지막 N개의 명령 표시:

`Get-History -Count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>
