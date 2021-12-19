---
layout: page
title: common/dotnet-restore (English)
description: "Restores the dependencies and tools of a .NET project."
content_hash: 9410c046f7733da08aceca06eb63323a79ced429
related_topics:
  - title: español version
    url: /es/common/dotnet-restore.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/dotnet-restore.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/dotnet-restore.html
    icon: bi bi-globe
---
# dotnet restore

Restores the dependencies and tools of a .NET project.
More information: <https://docs.microsoft.com/dotnet/core/tools/dotnet-restore>.

- Restore dependencies for a .NET project or solution in the current directory:

`dotnet restore`

- Restore dependencies for a .NET project or solution in a specific location:

`dotnet restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project_or_solution</span>

- Restore dependencies without caching the HTTP requests:

`dotnet restore --no-cache`

- Force all dependencies to be resolved even if the last restore was successful:

`dotnet restore --force`

- Restore dependencies using package source failures as warnings:

`dotnet restore --ignore-failed-sources`

- Restore dependencies with a specific verbosity level:

`dotnet restore --verbosity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quiet|minimal|normal|detailed|diagnostic</span>
