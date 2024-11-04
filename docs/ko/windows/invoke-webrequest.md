---
layout: page
title: windows/invoke-webrequest (한국어)
description: "HTTP/HTTPS 요청을 수행합니다."
content_hash: 9ad2e3b772369332c83b08d9af95e4659a5d215a
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/windows/invoke-webrequest.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/invoke-webrequest.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/invoke-webrequest.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/invoke-webrequest.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Invoke-WebRequest

HTTP/HTTPS 요청을 수행합니다.
참고: 이 명령어는 PowerShell을 통해서만 사용할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- URL의 내용을 파일로 다운로드:

`Invoke-WebRequest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>` -OutFile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>

- 폼 인코딩된 데이터 전송(`application/x-www-form-urlencoded` 타입의 POST 요청):

`Invoke-WebRequest -Method Post -Body @{ name='bob' } `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/form</span>

- 사용자 정의 HTTP 메서드 사용하여 추가 헤더가 있는 요청 전송:

`Invoke-WebRequest -Headers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@{ X-My-Header = '123' }</span>` -Method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PUT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>

- 적절한 content-type 헤더 지정하여 JSON 형식의 데이터 전송:

`Invoke-WebRequest -Body `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'{"name":"bob"}'</span>` -ContentType 'application/json' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/users/1234</span>

- 서버 인증을 위한 사용자 이름과 비밀번호 전달:

`Invoke-WebRequest -Headers @{ Authorization = "Basic "+ [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes("myusername:mypassword")) } `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>
