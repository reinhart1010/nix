---
layout: page
title: common/dotnet-run (English)
description: "Run a .NET application without explicit compile or launch commands."
content_hash: af3af5db8fe4d1e6a9ef9043f3a9ed313f3dc441
last_modified_at: 2023-10-16
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dotnet run

Run a .NET application without explicit compile or launch commands.
More information: <https://learn.microsoft.com/dotnet/core/tools/dotnet-run>.

- Run the project in the current directory:

`dotnet run`

- Run a specific project:

`dotnet run --project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.csproj</span>

- Run the project with specific arguments:

`dotnet run -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arg1=foo arg2=bar ...</span>

- Run the project using a target framework moniker:

`dotnet run --framework `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">net7.0</span>

- Specify architecture and OS, available since .NET 6 (Don't use `--runtime` with these options):

`dotnet run --arch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x86|x64|arm|arm64</span>` --os `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">win|win7|osx|linux|ios|android</span>
