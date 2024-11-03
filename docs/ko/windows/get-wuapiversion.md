---
layout: page
title: windows/get-wuapiversion (한국어)
description: "Windows 업데이트 에이전트 버전을 확인합니다. 외부 `PSWindowsUpdate` 모듈의 일부입니다."
content_hash: cda0e19a7a9c1776e5a5382d3fac24ea3286d3da
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/windows/get-wuapiversion.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/get-wuapiversion.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Get-WUApiVersion

Windows 업데이트 에이전트 버전을 확인합니다. 외부 `PSWindowsUpdate` 모듈의 일부입니다.
이 명령은 PowerShell에서만 실행할 수 있습니다.
더 많은 정보: <https://github.com/mgajda83/PSWindowsUpdate>.

- 현재 설치된 Windows 업데이트 에이전트 버전 확인:

`Get-WUApiVersion`

- 현재 설정 데이터를 이메일(SMTP)로 전송:

`Get-WUApiVersion -SendReport -PSWUSettings @{SmtpServer="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smtp_서버</span>`"; Port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smtp_포트</span>` From="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이메일_보낸이</span>`" To="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이메일_받는이</span>`"}`
