---
layout: page
title: common/dotnet-build (한국어)
description: ".NET 애플리케이션과 그 의존성을 빌드."
content_hash: 520aa5021df028554e2721680af34c115a3b33cc
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/dotnet-build.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/dotnet-build.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/dotnet-build.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/dotnet-build.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dotnet-build.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dotnet build

.NET 애플리케이션과 그 의존성을 빌드.
더 많은 정보: <https://learn.microsoft.com/dotnet/core/tools/dotnet-build>.

- 현재 디렉토리의 프로젝트나 솔루션 컴파일:

`dotnet build`

- 디버그 모드에서 .NET 프로젝트나 솔루션 컴파일:

`dotnet build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로젝트_또는_솔루션</span>

- 릴리즈 모드에서 컴파일:

`dotnet build --configuration `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Release</span>

- 의존성을 복원하지 않고 컴파일:

`dotnet build --no-restore`

- 특정 상세 수준으로 컴파일:

`dotnet build --verbosity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quiet|minimal|normal|detailed|diagnostic</span>

- 특정 런타임을 위해 컴파일:

`dotnet build --runtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">런타임_식별자</span>

- 출력 디렉토리 지정:

`dotnet build --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
