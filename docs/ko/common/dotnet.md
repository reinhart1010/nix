---
layout: page
title: common/dotnet (한국어)
description: "크로스 플랫폼 .NET Core용 명령줄 도구."
content_hash: 5a0037123c86dcae3a7f878d4cdddec9e00177b8
last_modified_at: 2024-11-01
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

크로스 플랫폼 .NET Core용 명령줄 도구.
`build`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
더 많은 정보: <https://learn.microsoft.com/dotnet/core/tools>.

- 새 .NET 프로젝트 초기화:

`dotnet new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">템플릿_짧은_이름</span>

- NuGet 패키지 복원:

`dotnet restore`

- 현재 디렉터리에서 .NET 프로젝트를 빌드하고 실행:

`dotnet run`

- 패키지된 dotnet 애플리케이션 실행 (런타임만 필요하며, 나머지 명령은 .NET Core SDK 설치 필요):

`dotnet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/application.dll</span>
