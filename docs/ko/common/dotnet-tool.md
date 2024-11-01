---
layout: page
title: common/dotnet-tool (한국어)
description: ".NET 도구를 관리하고 NuGet에서 게시된 도구를 검색."
content_hash: 450a4a60484bf45d9e8bd9f5e27f586317a8eb11
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/dotnet-tool.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/dotnet-tool.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dotnet-tool.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dotnet tool

.NET 도구를 관리하고 NuGet에서 게시된 도구를 검색.
더 많은 정보: <https://learn.microsoft.com/dotnet/core/tools/global-tools>.

- 전역 도구 설치 (`--global`은 로컬 도구에는 사용하지 않음):

`dotnet tool install --global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dotnetsay</span>

- 로컬 도구 매니페스트에 정의된 도구 설치:

`dotnet tool restore`

- 특정 전역 도구 업데이트 (`--global`은 로컬 도구에는 사용하지 않음):

`dotnet tool update --global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도구_이름</span>

- 전역 도구 제거 (`--global`은 로컬 도구에는 사용하지 않음):

`dotnet tool uninstall --global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도구_이름</span>

- 설치된 전역 도구 나열 (`--global`은 로컬 도구에는 사용하지 않음):

`dotnet tool list --global`

- NuGet에서 도구 검색:

`dotnet tool search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_어구</span>

- 도움말 표시:

`dotnet tool --help`
