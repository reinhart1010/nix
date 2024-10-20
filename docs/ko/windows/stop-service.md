---
layout: page
title: windows/stop-service (한국어)
description: "실행 중인 서비스를 중지합니다."
content_hash: 599e5493b85317b07a4f68b8f5f65e4bec4dc4c0
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/windows/stop-service.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Stop-Service

실행 중인 서비스를 중지합니다.
참고: 이 명령은 PowerShell을 통해서만 사용할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/stop-service>.

- 로컬 컴퓨터의 서비스 중지:

`Stop-Service -Name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름</span>

- 표시 이름을 사용하여 서비스 중지:

`Stop-Service -DisplayName "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>`"`

- 종속 서비스가 있는 서비스 중지:

`Stop-Service -Name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름</span>` -Force -Confirm`
