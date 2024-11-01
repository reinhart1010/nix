---
layout: page
title: common/dotnet-add-package (한국어)
description: "프로젝트 파일에 .NET 패키지 참조 추가 또는 업데이트."
content_hash: 29945ecea4bff96d4836626127bb412ad56d5d62
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/dotnet-add-package.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dotnet-add-package.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dotnet add package

프로젝트 파일에 .NET 패키지 참조 추가 또는 업데이트.
더 많은 정보: <https://learn.microsoft.com/dotnet/core/tools/dotnet-add-package>.

- 현재 디렉토리의 프로젝트에 패키지 추가:

`dotnet add package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 특정 프로젝트에 패키지 추가:

`dotnet add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.csproj</span>` package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 특정 버전의 패키지를 프로젝트에 추가:

`dotnet add package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.0.0</span>

- 특정 NuGet 소스를 사용하여 패키지 추가:

`dotnet add package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://api.nuget.org/v3/index.json</span>

- 특정 프레임워크를 대상으로 할 때만 패키지 추가:

`dotnet add package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` --framework `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">net7.0</span>

- 패키지를 복원할 디렉토리 지정 후 추가 (`~/.nuget/packages` 기본값):

`dotnet add package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` --package-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
