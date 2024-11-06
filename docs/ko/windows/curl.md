---
layout: page
title: windows/curl (한국어)
description: "PowerShell에서는 원본 `curl` 프로그램(<https://curl.se>)이 제대로 설치되지 않은 경우 이 명령이 `Invoke-WebRequest`의 별칭일 수 있습니다."
content_hash: 8fd0c5c7f9193061dd15305d8f9b4d72e4eba7c9
last_modified_at: 2024-11-06
related_topics:
  - title: বাংলা version
    url: /bn/windows/curl.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/windows/curl.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/curl.html
    icon: bi bi-globe
  - title: español version
    url: /es/windows/curl.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/curl.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/curl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/curl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/curl.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/curl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# curl

PowerShell에서는 원본 `curl` 프로그램(<https://curl.se>)이 제대로 설치되지 않은 경우 이 명령이 `Invoke-WebRequest`의 별칭일 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- 원본 `curl` 명령에 대한 문서 보기:

`tldr curl -p common`

- PowerShell의 `Invoke-WebRequest` 명령에 대한 문서 보기:

`tldr invoke-webrequest`

- `curl`이 제대로 설치되었는지 버전 번호를 출력하여 확인. 이 명령이 오류로 평가된다면, PowerShell이 이 명령을 `Invoke-WebRequest`로 대체했을 수 있습니다:

`curl --version`
