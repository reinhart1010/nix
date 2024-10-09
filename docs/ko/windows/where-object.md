---
layout: page
title: windows/where-object (한국어)
description: "속성 값에 따라 컬렉션에서 개체를 선택합니다."
content_hash: 8bac48cd2b1150775f5ce9e5b7a6af258b3e5af0
last_modified_at: 2024-10-09
related_topics:
  - title: English version
    url: /en/windows/where-object.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/where-object.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/where-object.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Where-Object

속성 값에 따라 컬렉션에서 개체를 선택합니다.
참고: 이 명령은 PowerShell을 통해서만 사용할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/where-object>.

- 별칭을 이름으로 필터링:

`Get-Alias | Where-Object -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">속성</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eq</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 현재 중지된 모든 서비스 나열. `$_` 자동 변수는 `Where-Object` cmdlet에 전달되는 각 개체를 나타냄:

`Get-Service | Where-Object {$_.Status -eq "Stopped"}`

- 여러 조건 사용:

`Get-Module -ListAvailable | Where-Object { $_.Name -NotLike "Microsoft*" -And $_.Name -NotLike "PS*" }`
