---
layout: page
title: windows/wait-process (한국어)
description: "더 많은 입력을 수락하기 전에 프로세스가 중지될 때까지 기다립니다."
content_hash: ea56fcc35ce189b1cd5e102c3cf93fd3098beebb
last_modified_at: 2024-10-10
related_topics:
  - title: English version
    url: /en/windows/wait-process.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Wait-Process

더 많은 입력을 수락하기 전에 프로세스가 중지될 때까지 기다립니다.
참고: 이 명령은 PowerShell을 통해서만 사용할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/wait-process>.

- 프로세스 중지 및 기다리기:

`Stop-Process -Id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_아이디</span>`; Wait-Process -Id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_아이디</span>

- 지정된 시간 동안 프로세스 기다리기:

`Wait-Process -Name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_이름</span>` -Timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>
