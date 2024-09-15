---
layout: page
title: common/az-bicep (한국어)
description: "Bicep CLI 명령어 집합."
content_hash: 06c7369c1d9234fd354b79ca008a10182ad4b38d
last_modified_at: 2024-09-15
related_topics:
  - title: English version
    url: /en/common/az-bicep.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/az-bicep.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/az-bicep.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># az bicep

Bicep CLI 명령어 집합.
`azure-cli`의 일부 (`az`라고도 함).
더 많은 정보: <https://learn.microsoft.com/cli/azure/bicep>.

- Bicep CLI 설치:

`az bicep install`

- Bicep 파일 빌드:

`az bicep build --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.bicep</span>

- ARM 템플릿 파일을 Bicep 파일로 디컴파일 하려고 시도:

`az bicep decompile --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/템플릿_파일.json</span>

- Bicep CLI를 최신 버전으로 업그레이드:

`az bicep upgrade`

- 설치된 Bicep CLI 버전을 표시:

`az bicep version`

- 사용 가능한 모든 Bicep CLI 버전 나열:

`az bicep list-versions`

- Bicep CLI 설치 삭제:

`az bicep uninstall`
