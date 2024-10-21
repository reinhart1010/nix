---
layout: page
title: windows/set-location (한국어)
description: "현재 작업 디렉토리를 표시하거나 다른 디렉토리로 이동합니다."
content_hash: c219e22e0d02dbdf7bb970ee84413f6010ab3bb2
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/windows/set-location.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/set-location.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/set-location.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Set-Location

현재 작업 디렉토리를 표시하거나 다른 디렉토리로 이동합니다.
이 명령어는 PowerShell을 통해서만 사용할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/set-location>.

- 지정된 디렉토리로 이동:

`Set-Location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\폴더</span>

- 다른 드라이브의 특정 디렉토리로 이동:

`Set-Location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\폴더</span>

- 지정된 디렉토리의 위치 표시:

`Set-Location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\폴더</span>` -PassThru`

- 현재 디렉토리의 상위 디렉토리로 이동:

`Set-Location ..`

- 현재 사용자의 홈 디렉토리로 이동:

`Set-Location ~`

- 이전에 선택한 디렉토리로 돌아가기/앞으로 이동:

`Set-Location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-|+</span>

- 현재 드라이브의 루트 디렉토리로 이동:

`Set-Location \`
