---
layout: page
title: windows/tee-object (한국어)
description: "명령어 출력을 파일 또는 변수에 저장하고 파이프라인으로 전달합니다."
content_hash: 227fb9d9db9c61765be5a4c254ea060d3eb55296
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/windows/tee-object.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/tee-object.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Tee-Object

명령어 출력을 파일 또는 변수에 저장하고 파이프라인으로 전달합니다.
참고: 이 명령어는 PowerShell을 통해서만 사용할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/tee-object>.

- 프로세스를 파일과 콘솔에 출력:

`Get-Process | Tee-Object -FilePath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>

- 프로세스를 변수와 `Select-Object`에 출력:

`Get-Process notepad | Tee-Object -Variable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">proc</span>` | Select-Object processname,handles`
