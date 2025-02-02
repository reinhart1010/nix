---
layout: page
title: windows/get-date (한국어)
description: "현재 날짜와 시간을 가져옵니다."
content_hash: 46faa9292f295837187069e4f328b344bd17fbb8
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/windows/get-date.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Get-Date

현재 날짜와 시간을 가져옵니다.
참고: 이 명령은 PowerShell을 통해서만 사용할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/get-date>.

- 현재 날짜와 시간을 표시:

`Get-Date`

- .NET 형식 지정자로 현재 날짜와 시간 표시:

`Get-Date -Format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yyyy-MM-dd HH:mm:ss</span>`"`

- UTC 및 ISO 8601 형식으로 현재 날짜와 시간 표시:

`(Get-Date).ToUniversalTime()`

- 유닉스 타임스탬프 변환:

`Get-Date -UnixTimeSeconds `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1577836800</span>
