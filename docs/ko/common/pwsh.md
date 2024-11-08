---
layout: page
title: common/pwsh (한국어)
description: "시스템 관리를 위해 특별히 설계된 명령줄 셸 및 스크립팅 언어."
content_hash: a3d9205b7755df1821c214431937f14e218d42af
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/pwsh.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/pwsh.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pwsh.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/pwsh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pwsh

시스템 관리를 위해 특별히 설계된 명령줄 셸 및 스크립팅 언어.
이 명령은 PowerShell 버전 6 이상(또는 PowerShell Core 및 크로스 플랫폼 PowerShell)을 의미합니다.
원래 Windows 버전(5.1 이하, 레거시 Windows PowerShell이라고도 함)을 사용하려면 `pwsh` 대신 `powershell`을 사용하세요.
더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_pwsh>.

- 대화형 셸 세션 시작:

`pwsh`

- 시작 구성 파일을 로드하지 않고 대화형 셸 세션 시작:

`pwsh -NoProfile`

- 특정 명령 실행:

`pwsh -Command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'powershell is executed'</span>`"`

- 특정 스크립트 실행:

`pwsh -File `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.ps1</span>

- 특정 버전의 PowerShell로 세션 시작:

`pwsh -Version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 시작 명령 실행 후 셸이 종료되지 않도록 방지:

`pwsh -NoExit`

- PowerShell에 전송되는 데이터 형식 설명:

`pwsh -InputFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Text|XML</span>

- PowerShell 출력 형식 결정:

`pwsh -OutputFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Text|XML</span>
