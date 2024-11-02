---
layout: page
title: common/dotnet-restore (한국어)
description: ".NET 프로젝트의 의존성과 도구를 복원합니다."
content_hash: 62ca6294614fab658e0402a7870bcbdf87914b7a
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/dotnet-restore.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/dotnet-restore.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/dotnet-restore.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/dotnet-restore.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dotnet restore

.NET 프로젝트의 의존성과 도구를 복원합니다.
더 많은 정보: <https://learn.microsoft.com/dotnet/core/tools/dotnet-restore>.

- 현재 디렉터리의 .NET 프로젝트 또는 솔루션의 의존성 복원:

`dotnet restore`

- 특정 위치의 .NET 프로젝트 또는 솔루션의 의존성 복원:

`dotnet restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로젝트_또는_솔루션</span>

- HTTP 요청을 캐시하지 않고 의존성 복원:

`dotnet restore --no-cache`

- 마지막 복원이 성공했더라도 모든 의존성을 강제로 해결:

`dotnet restore --force`

- 패키지 소스 실패를 경고로 처리하여 의존성 복원:

`dotnet restore --ignore-failed-sources`

- 특정 상세 수준으로 의존성 복원:

`dotnet restore --verbosity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quiet|minimal|normal|detailed|diagnostic</span>
