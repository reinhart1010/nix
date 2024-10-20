---
layout: page
title: windows/start-service (한국어)
description: "중지된 서비스를 시작합니다."
content_hash: 04e23266739931f450749b9d908fe43bf27a338c
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/windows/start-service.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Start-Service

중지된 서비스를 시작합니다.
참고: 이 명령은 PowerShell을 통해서만 사용할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/start-service>.

- 서비스 이름을 사용하여 서비스 시작:

`Start-Service -Name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름</span>

- 서비스를 시작하지 않고 정보 표시:

`Start-Service -DisplayName *`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>`* -WhatIf`

- 비활성화된 서비스 시작:

`Set-Service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름</span>` -StartupType `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">manual</span>`; Start-Service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름</span>
