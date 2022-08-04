---
layout: page
title: common/dotnet (English)
description: "Cross platform .NET command-line tools for .NET Core."
content_hash: e3c0f7fc1a6d9c76a3e65c5f5e4a7c0dc7a2e73f
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
---
# dotnet

Cross platform .NET command-line tools for .NET Core.
Some subcommands such as `dotnet build` have their own usage documentation.
More information: <https://docs.microsoft.com/dotnet/core/tools>.

- Initialize a new .NET project:

`dotnet new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">template_short_name</span>

- Restore NuGet packages:

`dotnet restore`

- Build and execute the .NET project in the current directory:

`dotnet run`

- Run a packaged dotnet application (only needs the runtime, the rest of the commands require the .NET Core SDK installed):

`dotnet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/application.dll</span>
