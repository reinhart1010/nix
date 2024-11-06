---
layout: page
title: windows/cd (한국어)
description: "현재 작업 중인 디렉토리를 표시하거나 다른 디렉토리로 이동."
content_hash: 2c0b2d1ce28b92bb45af5f3a977e57571912a812
last_modified_at: 2024-11-06
related_topics:
  - title: বাংলা version
    url: /bn/windows/cd.html
    icon: bi bi-globe
  - title: català version
    url: /ca/windows/cd.html
    icon: bi bi-globe
  - title: čeština version
    url: /cs/windows/cd.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/windows/cd.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/cd.html
    icon: bi bi-globe
  - title: español version
    url: /es/windows/cd.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/cd.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/cd.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/cd.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/cd.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/cd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/cd.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/cd.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/cd.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/windows/cd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cd

현재 작업 중인 디렉토리를 표시하거나 다른 디렉토리로 이동.
PowerShell에서는 이 명령이 `Set-Location`의 별칭입니다. 이 문서는 Command Prompt(`cmd`) 버전의 `cd`를 기반으로 합니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/cd>.

- PowerShell의 동등한 명령에 대한 문서 보기:

`tldr set-location`

- 현재 디렉토리의 경로 표시:

`cd`

- 같은 드라이브의 특정 디렉토리로 이동:

`cd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\디렉토리</span>

- 다른 [d]rive의 특정 디렉토리로 이동:

`cd /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\디렉토리</span>

- 현재 디렉토리의 상위 디렉토리로 이동:

`cd ..`

- 현재 사용자의 홈 디렉토리로 이동:

`cd %userprofile%`

- 현재 드라이브의 루트로 이동:

`cd \`
