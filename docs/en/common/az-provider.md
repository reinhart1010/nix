---
layout: page
title: common/az-provider (English)
description: "Manage resource providers."
content_hash: 511c17eaf81203f9d0b340378b211c017c7376d9
last_modified_at: 2023-10-15
---
# az provider

Manage resource providers.
Part of `azure-cli` (also known as `az`).
More information: <https://learn.microsoft.com/cli/azure/provider>.

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
