---
layout: page
title: common/dotnet (English)
description: "Cross platform .NET command-line tools for .NET Core."
content_hash: f7827da80e3efece84387c938350bff737a9f902
related_topics:
  - title: Deutsch version
    url: /de/common/dotnet.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/dotnet.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dotnet.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dotnet.html
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
---
# dotnet

Cross platform .NET command-line tools for .NET Core.
Some subcommands such as `dotnet build` have their own usage documentation.
More information: <https://learn.microsoft.com/dotnet/core/tools>.

- Initialize a new .NET project:

`dotnet new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">template_short_name</span>

- Restore NuGet packages:

`dotnet restore`

- Build and execute the .NET project in the current directory:

`dotnet run`

- Run a packaged dotnet application (only needs the runtime, the rest of the commands require the .NET Core SDK installed):

`dotnet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/application.dll</span>
