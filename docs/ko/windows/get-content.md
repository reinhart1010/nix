---
layout: page
title: windows/get-content (한국어)
description: "지정된 위치에 있는 항목의 내용을 가져옵니다."
content_hash: 5c0bd2006f342e7f8961af058dde9f9be9d7d964
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/windows/get-content.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/get-content.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Get-Content

지정된 위치에 있는 항목의 내용을 가져옵니다.
참고: 이 명령은 PowerShell을 통해서만 사용할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/get-content>.

- 파일의 내용 표시:

`Get-Content -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>

- 파일의 처음 몇 줄 표시:

`Get-Content -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>` -TotalCount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- 파일의 내용을 표시하고 `Ctrl + C`를 누를 때까지 계속 읽기:

`Get-Content -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>` -Wait`
