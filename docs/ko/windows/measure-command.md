---
layout: page
title: windows/measure-command (한국어)
description: "스크립트 블록 및 cmdlet을 실행하는 데 걸리는 시간을 측정합니다."
content_hash: 05b622361fa2a7a9c9245a953347013184226172
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/windows/measure-command.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/measure-command.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Measure-Command

스크립트 블록 및 cmdlet을 실행하는 데 걸리는 시간을 측정합니다.
참고: 이 명령어는 PowerShell을 통해서만 사용할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/measure-command>.

- 명령어를 실행하는 데 걸리는 시간 측정:

`Measure-Command { `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` }`

- `Measure-Command`에 파이프 입력 (파이프된 객체는 `Measure-Command`의 Expression 매개변수에 전달된 스크립트 블록에서 사용 가능):

`10, 20, 50 | Measure-Command -Expression { for ($i=0; $i -lt $_; $i++) {$i} }`
