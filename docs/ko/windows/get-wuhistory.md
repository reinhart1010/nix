---
layout: page
title: windows/get-wuhistory (한국어)
description: "Windows Update에서 설치된 업데이트의 기록을 가져옵니다. 외부 `PSWindowsUpdate` 모듈의 일부입니다."
content_hash: 9810634c6f742fd3136a09fe849e9222d2fa2571
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/windows/get-wuhistory.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Get-WUHistory

Windows Update에서 설치된 업데이트의 기록을 가져옵니다. 외부 `PSWindowsUpdate` 모듈의 일부입니다.
이 명령은 PowerShell에서만 실행할 수 있습니다.
더 많은 정보: <https://github.com/mgajda83/PSWindowsUpdate>.

- 업데이트 기록 목록 가져오기:

`Get-WUHistory`

- 최근 10개의 설치된 업데이트 나열:

`Get-WUHistory -Last `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- 특정 날짜부터 오늘까지 설치된 모든 업데이트 나열:

`Get-WUHistory -MaxDate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">날짜</span>

- 지난 24시간 동안 설치된 모든 업데이트 나열:

`Get-WUHistory -MaxDate (Get-Date).AddDays(-1)`

- 결과를 이메일(SMTP)로 전송:

`Get-WUHistory -SendReport -PSWUSettings @{SmtpServer="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smtp_서버</span>`"; Port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smtp_포트</span>` From="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">발신자_이메일</span>`" To="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">수신자_이메일</span>`"}`
