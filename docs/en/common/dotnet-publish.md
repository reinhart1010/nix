---
layout: page
title: common/dotnet-publish (English)
description: "Publish a .NET application and its dependencies to a directory for deployment to a hosting system."
content_hash: 7fc484ffe253483a8af7b117b6bd7865d0eb685e
related_topics:
  - title: español version
    url: /es/common/dotnet-publish.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/dotnet-publish.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/dotnet-publish.html
    icon: bi bi-globe
---
# dotnet publish

Publish a .NET application and its dependencies to a directory for deployment to a hosting system.
More information: <https://learn.microsoft.com/dotnet/core/tools/dotnet-publish>.

- Compile a .NET project in release mode:

`dotnet publish --configuration Release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project_file</span>

- Publish the .NET Core runtime with your application for the specified runtime:

`dotnet publish --self-contained true --runtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">runtime_identifier</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project_file</span>

- Package the application into a platform-specific single-file executable:

`dotnet publish --runtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">runtime_identifier</span>` -p:PublishSingleFile=true `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project_file</span>

- Trim unused libraries to reduce the deployment size of an application:

`dotnet publish --self-contained true --runtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">runtime_identifier</span>` -p:PublishTrimmed=true `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project_file</span>

- Compile a .NET project without restoring dependencies:

`dotnet publish --no-restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project_file</span>

- Specify the output directory:

`dotnet publish --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project_file</span>
