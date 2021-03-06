---
layout: page
title: common/az-bicep (English)
description: "Bicep CLI command group."
content_hash: 343bb8f4a529775dbb288522ba53198cfb36a81b
---
# az bicep

Bicep CLI command group.
Part of `azure-cli`.
More information: <https://docs.microsoft.com/cli/azure/bicep>.

- Install Bicep CLI:

`az bicep install`

- Build a Bicep file:

`az bicep build --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bicep</span>

- Attempt to decompile an ARM template file to a Bicep file:

`az bicep decompile --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/template_file.json</span>

- Upgrade Bicep CLI to the latest version:

`az bicep upgrade`

- Display the installed version of Bicep CLI:

`az bicep version`

- List all available versions of Bicep CLI:

`az bicep list-versions`

- Uninstall Bicep CLI:

`az bicep uninstall`
