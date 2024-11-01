---
layout: page
title: common/dotnet-publish (한국어)
description: ".NET 애플리케이션과 그 의존성을 호스팅 시스템에 배포하기 위해 디렉터리에 게시."
content_hash: 877cde5ac313bac80aa87f35257b4da0b05ee07e
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/dotnet-publish.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/dotnet-publish.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/dotnet-publish.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/dotnet-publish.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dotnet-publish.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dotnet publish

.NET 애플리케이션과 그 의존성을 호스팅 시스템에 배포하기 위해 디렉터리에 게시.
더 많은 정보: <https://learn.microsoft.com/dotnet/core/tools/dotnet-publish>.

- .NET 프로젝트를 릴리스 모드로 컴파일:

`dotnet publish --configuration Release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로젝트_파일</span>

- 지정된 런타임에 대해 .NET Core 런타임을 애플리케이션과 함께 게시:

`dotnet publish --self-contained true --runtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">런타임_식별자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로젝트_파일</span>

- 애플리케이션을 플랫폼별 단일 파일 실행 파일로 패키징:

`dotnet publish --runtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">런타임_식별자</span>` -p:PublishSingleFile=true `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로젝트_파일</span>

- 사용하지 않는 라이브러리를 제거하여 애플리케이션의 배포 크기 줄이기:

`dotnet publish --self-contained true --runtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">런타임_식별자</span>` -p:PublishTrimmed=true `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로젝트_파일</span>

- 의존성을 복원하지 않고 .NET 프로젝트 컴파일:

`dotnet publish --no-restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로젝트_파일</span>

- 출력 디렉터리 지정:

`dotnet publish --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로젝트_파일</span>
