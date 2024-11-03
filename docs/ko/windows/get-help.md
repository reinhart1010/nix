---
layout: page
title: windows/get-help (한국어)
description: "PowerShell 명령(별칭, cmdlet, 함수)에 대한 도움말 정보와 문서를 표시."
content_hash: d9170b15193222f05db759482e585bdf18dea732
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/windows/get-help.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/get-help.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Get-Help

PowerShell 명령(별칭, cmdlet, 함수)에 대한 도움말 정보와 문서를 표시.
이 명령은 PowerShell을 통해서만 실행할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/get-help>.

- 특정 PowerShell 명령에 대한 일반적인 도움말 정보 표시:

`Get-Help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 특정 PowerShell 명령에 대한 자세한 문서 표시:

`Get-Help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` -Detailed`

- 특정 PowerShell 명령에 대한 전체 기술 문서 표시:

`Get-Help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` -Full`

- 특정 PowerShell 명령의 특정 매개변수 문서만 표시 (가능한 경우 `*`을 사용하여 모든 매개변수 표시):

`Get-Help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` -Parameter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">매개변수</span>

- cmdlet의 예제만 표시 (가능한 경우):

`Get-Help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` -Examples`

- 사용 가능한 모든 cmdlet 도움말 페이지 나열:

`Get-Help *`

- `Update-Help`를 사용하여 현재 도움말 및 문서 지식베이스 업데이트:

`Update-Help`

- 기본 웹 브라우저에서 PowerShell 명령 문서의 온라인 버전 보기:

`Get-Help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` -Online`
