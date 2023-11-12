---
layout: page
title: common/msbuild (English)
description: "The Microsoft build tool for Visual Studio project solutions."
content_hash: c9fbd4e7f2fb6c0f29d0afdb637e7ba9757924b9
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# msbuild

The Microsoft build tool for Visual Studio project solutions.
More information: <https://learn.microsoft.com/visualstudio/msbuild>.

- Build the first project file in the current directory:

`msbuild`

- Build a specific project file:

`msbuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project_file</span>

- Set one or more semicolon-separated targets to build:

`msbuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project_file</span>` /target:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">targets</span>

- Set one or more semicolon-separated properties:

`msbuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project_file</span>` /property:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name=value</span>

- Set the build tools version to use:

`msbuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project_file</span>` /toolsversion:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Display detailed information at the end of the log about how the project was configured:

`msbuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project_file</span>` /detailedsummary`

- Display detailed help information:

`msbuild /help`
