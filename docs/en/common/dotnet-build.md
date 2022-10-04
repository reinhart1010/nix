---
layout: page
title: common/dotnet-build (English)
description: "Builds a .NET application and its dependencies."
content_hash: 1dde27068e92de06c3a49eeb45265985f8ad52dc
related_topics:
  - title: español version
    url: /es/common/dotnet-build.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/dotnet-build.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/dotnet-build.html
    icon: bi bi-globe
---
# dotnet build

Builds a .NET application and its dependencies.
More information: <https://learn.microsoft.com/dotnet/core/tools/dotnet-build>.

- Compile the project or solution in the current directory:

`dotnet build`

- Compile a .NET project or solution in debug mode:

`dotnet build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project_or_solution</span>

- Compile in release mode:

`dotnet build --configuration `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Release</span>

- Compile without restoring dependencies:

`dotnet build --no-restore`

- Compile with a specific verbosity level:

`dotnet build --verbosity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quiet|minimal|normal|detailed|diagnostic</span>

- Compile for a specific runtime:

`dotnet build --runtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">runtime_identifier</span>

- Specify the output directory:

`dotnet build --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
