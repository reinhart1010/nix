---
layout: page
title: windows/measure-object (한국어)
description: "객체의 숫자 속성과 문자열 객체(예: 텍스트 파일)의 문자, 단어 및 줄을 계산합니다."
content_hash: c3db086082accaa52a812f44a89109a925e4ccd8
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/windows/measure-object.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/measure-object.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Measure-Object

객체의 숫자 속성과 문자열 객체(예: 텍스트 파일)의 문자, 단어 및 줄을 계산합니다.
참고: 이 명령어는 PowerShell을 통해서만 사용할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/measure-object>.

- 디렉토리의 파일 및 폴더 수 계산:

`Get-ChildItem | Measure-Object`

- `Measure-Command`에 파이프 입력 (파이프된 객체는 `Measure-Command`의 Expression 매개변수에 전달된 스크립트 블록에서 사용 가능):

`"One", "Two", "Three", "Four" | Set-Content -Path "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>`"; Get-Content "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>`"; | Measure-Object -Character -Line -Word`
