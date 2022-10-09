---
layout: page
title: common/az-provider (English)
description: "Manage resource providers."
content_hash: 86e729035b441a42f2865a86237e2fae7bd0c225
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># az provider

Manage resource providers.
Part of `azure-cli`.
More information: <https://docs.microsoft.com/cli/azure/provider>.

- Register a provider:

`az provider register --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Microsoft.PolicyInsights</span>

- Unregister a provider:

`az provider unregister --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Microsoft.Automation</span>

- List all providers for a subscription:

`az provider list`

- Show information about a specific provider:

`az provider show --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Microsoft.Storage</span>

- List all resource types for a specific provider:

`az provider list --query "[?namespace=='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Microsoft.Network</span>`'].resourceTypes[].resourceType"`
