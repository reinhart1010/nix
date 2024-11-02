---
layout: page
title: common/dotnet-run (한국어)
description: "명시적인 컴파일 또는 실행 명령 없이 .NET 애플리케이션을 실행합니다."
content_hash: 3d791a65d9acc7ba409ab41dee67167bd688371b
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/dotnet-run.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dotnet run

명시적인 컴파일 또는 실행 명령 없이 .NET 애플리케이션을 실행합니다.
더 많은 정보: <https://learn.microsoft.com/dotnet/core/tools/dotnet-run>.

- 현재 디렉토리의 프로젝트 실행:

`dotnet run`

- 특정 프로젝트 실행:

`dotnet run --project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.csproj</span>

- 특정 인수를 사용하여 프로젝트 실행:

`dotnet run -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arg1=foo arg2=bar ...</span>

- 대상 프레임워크 모니커를 사용하여 프로젝트 실행:

`dotnet run --framework `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">net7.0</span>

- .NET 6부터 사용 가능한 아키텍처 및 OS 지정 (이 옵션들과 함께 `--runtime` 사용 금지):

`dotnet run --arch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x86|x64|arm|arm64</span>` --os `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">win|win7|osx|linux|ios|android</span>
