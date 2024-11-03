---
layout: page
title: windows/get-wusettings (한국어)
description: "현재 Windows Update 에이전트 구성을 가져옵니다. 외부 `PSWindowsUpdate` 모듈의 일부입니다."
content_hash: 0db72d58cc614b09cb60f9e9ef04eb4eb612b8f2
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/windows/get-wusettings.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/get-wusettings.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Get-WUSettings

현재 Windows Update 에이전트 구성을 가져옵니다. 외부 `PSWindowsUpdate` 모듈의 일부입니다.
이 명령은 PowerShell에서만 실행할 수 있습니다.
더 많은 정보: <https://github.com/mgajda83/PSWindowsUpdate>.

- 현재 Windows Update 에이전트 구성 가져오기:

`Get-WUSettings`

- 현재 구성 데이터를 이메일(SMTP)로 전송:

`Get-WUSettings -SendReport -PSWUSettings @{SmtpServer="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smtp_서버</span>`"; Port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smtp_포트</span>` From="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이메일_보낸이</span>`" To="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이메일_받는이</span>`"}`
