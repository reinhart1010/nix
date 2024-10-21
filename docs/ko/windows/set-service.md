---
layout: page
title: windows/set-service (한국어)
description: "서비스를 시작, 중지 및 일시 중단하고 속성을 변경합니다."
content_hash: ae84b7d8226feb37b652e2909e4499647cd58449
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/windows/set-service.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Set-Service

서비스를 시작, 중지 및 일시 중단하고 속성을 변경합니다.
이 명령어는 PowerShell을 통해서만 사용할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/set-service>.

- 표시 이름 변경:

`Set-Service -Name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` -DisplayName "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>`"`

- 서비스 시작 유형 변경:

`Set-Service -Name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스명</span>` -StartupType `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Automatic</span>

- 서비스 설명 변경:

`Set-Service -Name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스명</span>` -Description "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">설명</span>`"`
