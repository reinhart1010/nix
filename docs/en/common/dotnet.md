---
layout: page
title: common/dotnet (English)
description: "Cross platform .NET command-line tools for .NET Core."
content_hash: 9d329e820a7f326a904fb93443010cd358ae117e
last_modified_at: 2024-10-05
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
tldri18n_status: 2
---
# dotnet

Cross platform .NET command-line tools for .NET Core.
Some subcommands such as `build` have their own usage documentation.
More information: <https://learn.microsoft.com/dotnet/core/tools>.

- Initialize a new .NET project:

`dotnet new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">template_short_name</span>

- Restore NuGet packages:

`dotnet restore`

- Build and execute the .NET project in the current directory:

`dotnet run`

- Run a packaged dotnet application (only needs the runtime, the rest of the commands require the .NET Core SDK installed):

`dotnet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/application.dll</span>
