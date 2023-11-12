---
layout: page
title: common/dotnet (한국어)
description: ".NET Core를 위한 크로스 플랫폼 .NET 명령어 도구."
content_hash: dd4ea010f656a1810510f920c699e270af83417e
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/dotnet.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/dotnet.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/dotnet.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dotnet.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/dotnet.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/dotnet.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/dotnet.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dotnet

.NET Core를 위한 크로스 플랫폼 .NET 명령어 도구.
더 많은 정보: <https://learn.microsoft.com/dotnet/core/tools>.

- 새 .NET 프로젝트 초기화하기:

`dotnet new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">짧은_템플릿_이름</span>

- nuget 패키지들 복구하기:

`dotnet restore`

- 현재 디렉토리에서 .NET 프로젝트를 빌드하고 실행하기:

`dotnet run`

- 패키지화 된 dotnet 어플리케이션을 실행하기(런타임만 필요하며, 나머지 명령어들은 .NET Core SDK 설치가 필요):

`dotnet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/어플리케이션.dll</span>
