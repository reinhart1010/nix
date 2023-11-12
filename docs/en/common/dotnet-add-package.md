---
layout: page
title: common/dotnet-add-package (English)
description: "Add or update a .NET package reference in a project file."
content_hash: 759a044172bf8de4b3a57b69734a5f71cb315292
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# dotnet add package

Add or update a .NET package reference in a project file.
More information: <https://learn.microsoft.com/dotnet/core/tools/dotnet-add-package>.

- Add a package to the project in the current directory:

`dotnet add package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Add a package to a specific project:

`dotnet add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.csproj</span>` package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Add a specific version of a package to the project:

`dotnet add package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.0.0</span>

- Add a package using a specific NuGet source:

`dotnet add package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://api.nuget.org/v3/index.json</span>

- Add a package only when targeting a specific framework:

`dotnet add package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --framework `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">net7.0</span>

- Add and specify the directory where to restore packages (`~/.nuget/packages` by default):

`dotnet add package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --package-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
