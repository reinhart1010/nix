---
layout: page
title: common/dotnet-add-reference (English)
description: "Add .NET project-to-project references."
content_hash: 0aa4ace899e546466a2b157a88050d6d44ff06bf
last_modified_at: 2023-10-18
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dotnet add reference

Add .NET project-to-project references.
More information: <https://learn.microsoft.com/dotnet/core/tools/dotnet-add-reference>.

- Add a reference to the project in the current directory:

`dotnet add reference `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/reference.csproj</span>

- Add a reference to the specific project:

`dotnet add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project.csproj</span>` reference `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/reference.csproj</span>
