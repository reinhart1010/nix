---
layout: page
title: windows/wget (한국어)
description: "원래 `wget` 프로그램 (<https://www.gnu.org/software/wget>)이 제대로 설치되지 않은 경우, PowerShell에서는 이 명령이 `Invoke-WebRequest`의 별칭일 수 있습니다."
content_hash: 45d36e482300e37e52d0a9ef1aafc9b16ee909c6
last_modified_at: 2024-10-14
related_topics:
  - title: বাংলা version
    url: /bn/windows/wget.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/windows/wget.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/wget.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/wget.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/wget.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/wget.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/wget.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/wget.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/wget.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># wget

원래 `wget` 프로그램 (<https://www.gnu.org/software/wget>)이 제대로 설치되지 않은 경우, PowerShell에서는 이 명령이 `Invoke-WebRequest`의 별칭일 수 있습니다.
참고: 버전 명령어가 오류를 반환하는 경우, PowerShell이 이 명령을 `Invoke-WebRequest`로 대체할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- 원래 `wget` 명령어의 문서 보기:

`tldr wget -p common`

- PowerShell의 `Invoke-WebRequest` 명령어의 문서 보기:

`tldr invoke-webrequest`

- 버전 표시:

`wget --version`
