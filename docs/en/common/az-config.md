---
layout: page
title: common/az-config (English)
description: "Manage Azure CLI configuration."
content_hash: af2a32717eb465ddb8934f0c4fda0a06f0290d9c
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/az-config.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/az-config.html
    icon: bi bi-globe
tldri18n_status: 2
---
# az config

Manage Azure CLI configuration.
Part of `azure-cli` (also known as `az`).
More information: <https://learn.microsoft.com/cli/azure/config>.

- Print all configurations:

`az config get`

- Print configurations for a specific section:

`az config get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">section_name</span>

- Set a configuration:

`az config set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">configuration_name</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Unset a configuration:

`az config unset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">configuration_name</span>
