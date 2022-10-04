---
layout: page
title: common/dotnet-tool (English)
description: "Manage .NET tools and search published tools in NuGet."
content_hash: e22734f0e15f215661d77f70834dcb1a8bfe9a7d
---
# dotnet tool

Manage .NET tools and search published tools in NuGet.
More information: <https://learn.microsoft.com/dotnet/core/tools/global-tools>.

- Install a global tool (don't use `--global` for local tools):

`dotnet tool install --global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dotnetsay</span>

- Install tools defined in the local tool manifest:

`dotnet tool restore`

- Update a specific global tool (don't use `--global` for local tools):

`dotnet tool update --global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tool_name</span>

- Uninstall a global tool (don't use `--global` for local tools):

`dotnet tool uninstall --global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tool_name</span>

- List installed global tools (don't use `--global` for local tools):

`dotnet tool list --global`

- Search tools in NuGet:

`dotnet tool search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>

- Display help:

`dotnet tool --help`
