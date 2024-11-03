---
layout: page
title: windows/get-command (한국어)
description: "현재 PowerShell 세션에서 사용 가능한 명령을 나열하고 가져옴."
content_hash: 39b40aa61f019a5e068e85146b3f734c0fdb5b83
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/windows/get-command.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/get-command.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Get-Command

현재 PowerShell 세션에서 사용 가능한 명령을 나열하고 가져옴.
이 명령은 PowerShell을 통해서만 실행 가능.
더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/get-command>.

- 현재 컴퓨터에서 사용 가능한 모든 PowerShell 명령(별칭, cmdlet, 함수) 나열:

`Get-Command`

- 현재 세션에서 사용 가능한 모든 PowerShell 명령 나열:

`Get-Command -ListImported`

- 컴퓨터에서 사용 가능한 PowerShell 별칭/cmdlet/함수만 나열:

`Get-Command -Type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">별칭|Cmdlet|함수</span>

- 현재 세션에서 PATH에 있는 프로그램이나 명령만 나열:

`Get-Command -Type Application`

- 모듈 이름으로 PowerShell 명령만 나열, 예: 유틸리티 관련 명령은 `Microsoft.PowerShell.Utility`:

`Get-Command -Module `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈</span>

- 이름으로 명령 정보(예: 버전 번호나 모듈 이름) 가져오기:

`Get-Command `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>
