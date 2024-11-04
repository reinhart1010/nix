---
layout: page
title: windows/install-module (한국어)
description: "PowerShell Gallery, NuGet 및 기타 리포지토리에서 PowerShell 모듈을 설치합니다."
content_hash: 51c779061f32c1aaac0854604606ab114e604408
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/windows/install-module.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/install-module.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Install-Module

PowerShell Gallery, NuGet 및 기타 리포지토리에서 PowerShell 모듈을 설치합니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/powershellget/install-module>.

- 모듈 설치 또는 최신 버전으로 업데이트:

`Install-Module `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈</span>

- 특정 버전의 모듈 설치:

`Install-Module `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈</span>` -RequiredVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 최소 버전을 사용하여 모듈 설치:

`Install-Module `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈</span>` -MinimumVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 모듈의 지원되는 버전 범위를 지정하여 설치:

`Install-Module `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈</span>` -MinimumVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">최소_버전</span>` -MaximumVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">최대_버전</span>

- 특정 리포지토리에 모듈 설치:

`Install-Module `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈</span>` -Repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리포지토리</span>

- 지정된 리포지토리들에서 모듈 설치:

`Install-Module `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈</span>` -Repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리포지토리1, 리포지토리2, ...</span>

- 모듈을 모든 사용자 또는 현재 사용자에게 설치:

`Install-Module `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈</span>` -Scope `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AllUsers|CurrentUser</span>

- `Install-Module`을 통해 설치, 업그레이드 또는 제거될 모듈을 확인하기 위한 테스트 실행:

`Install-Module `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈</span>` -WhatIf`
