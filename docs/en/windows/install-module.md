---
layout: page
title: windows/install-module (English)
description: "Install PowerShell modules from PowerShell Gallery, NuGet, and other repositories."
content_hash: a52ff43a4d28663c03cf153ee37281271e349759
last_modified_at: 2023-12-01
tldri18n_status: 2
---
# Install-Module

Install PowerShell modules from PowerShell Gallery, NuGet, and other repositories.
More information: <https://learn.microsoft.com/powershell/module/powershellget/install-module>.

- Install a module, or update it to the latest available version:

`Install-Module `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module</span>

- Install a module with a specific version:

`Install-Module `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module</span>` -RequiredVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Install a module no earlier than a specific version:

`Install-Module `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module</span>` -MinimumVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Specify a range of supported versions (inclusive) of the required module:

`Install-Module `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module</span>` -MinimumVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minimum_version</span>` -MaximumVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">maximum_version</span>

- Install module from a specific repository:

`Install-Module `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module</span>` -Repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>

- Install module from specific repositories:

`Install-Module `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module</span>` -Repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository1 , repository2 , ...</span>

- Install the module for all/current user:

`Install-Module `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module</span>` -Scope `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AllUsers|CurrentUser</span>

- Perform a dry run to determine which modules will be installed, upgraded, or removed through `Install-Module`:

`Install-Module `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module</span>` -WhatIf`
