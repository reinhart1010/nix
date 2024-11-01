---
layout: page
title: windows/powershell (한국어)
description: "시스템 관리를 위해 특별히 설계된 명령줄 쉘 및 스크립팅 언어입니다."
content_hash: f6a3149c6f14d7f89b638a265efd5c867681e768
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/windows/powershell.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/powershell.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/powershell.html
    icon: bi bi-globe
tldri18n_status: 2
---
# powershell

시스템 관리를 위해 특별히 설계된 명령줄 쉘 및 스크립팅 언어입니다.
이 명령어는 PowerShell 버전 5.1 이하 (레거시 Windows PowerShell이라고도 함)를 참조합니다. 더 새로운, 크로스 플랫폼 버전의 PowerShell (PowerShell Core라고도 함)을 사용하려면 `pwsh` 대신 `powershell`을 사용하세요.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/powershell>.

- 대화형 쉘 세션 시작:

`powershell`

- 시작 설정을 로드하지 않고 대화형 쉘 세션 시작:

`powershell -NoProfile`

- 특정 명령어 실행:

`powershell -Command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'powershell is executed'</span>`"`

- 특정 스크립트 실행:

`powershell -File `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.ps1</span>

- 특정 버전의 PowerShell로 세션 시작:

`powershell -Version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 시작 명령을 실행한 후 쉘 종료 방지:

`powershell -NoExit`

- PowerShell에 전달되는 데이터의 형식 설명:

`powershell -InputFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Text|XML</span>

- PowerShell에서 출력되는 데이터의 형식 설명:

`powershell -OutputFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Text|XML</span>
