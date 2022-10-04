---
layout: page
title: common/az-config (English)
description: "Manage Azure CLI configuration."
content_hash: afff0b867e60e5accbe4e99ab6ebfb6dabd0036d
---
# az config

Manage Azure CLI configuration.
Part of `azure-cli`.
More information: <https://learn.microsoft.com/cli/azure/config>.

- Print all configurations:

`az config get`

- Print configurations for a specific section:

`az config get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">section_name</span>

- Set a configuration:

`az config set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">configuration_name</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Unset a configuration:

`az config unset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">configuration_name</span>
