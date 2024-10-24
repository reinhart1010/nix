---
layout: page
title: windows/select-string (한국어)
description: "PowerShell에서 문자열과 파일에서 텍스트를 찾습니다."
content_hash: 4ffb68183d9cc58888bab2dd031cd54ae923f884
last_modified_at: 2024-10-24
related_topics:
  - title: English version
    url: /en/windows/select-string.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/select-string.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/select-string.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Select-String

PowerShell에서 문자열과 파일에서 텍스트를 찾습니다.
참고: 이 명령어는 PowerShell을 통해서만 사용할 수 있습니다.
`Select-String`을 UNIX의 `grep`이나 Windows의 `findstr.exe`와 유사하게 사용할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/select-string>.

- 파일 내에서 패턴 검색:

`Select-String -Path "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>`" -Pattern '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`'`

- 정확한 문자열 검색 (정규식 비활성화):

`Select-String -SimpleMatch "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정확한_문자열</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>

- 현재 디렉토리의 모든 `.ext` 파일에서 패턴 검색:

`Select-String -Path "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>`" -Pattern '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`'`

- 패턴과 일치하는 줄 앞뒤의 지정된 줄 수 캡처:

`Select-String --Context `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2,3</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>

- `stdin`에서 패턴과 일치하지 않는 줄 검색:

`Get-Content `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>` | Select-String --NotMatch "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`"`
