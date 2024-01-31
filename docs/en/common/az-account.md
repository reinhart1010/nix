---
layout: page
title: common/az-account (English)
description: "Manage Azure subscription information."
content_hash: ea1bb01af785df91d375187c000eca85eef0a6f8
last_modified_at: 2024-01-31
related_topics:
  - title: español version
    url: /es/common/az-account.html
    icon: bi bi-globe
tldri18n_status: 2
---
# az account

Manage Azure subscription information.
Part of `azure-cli` (also known as `az`).
More information: <https://learn.microsoft.com/cli/azure/account>.

- List all subscriptions for the logged in account:

`az account list`

- Set a `subscription` to be the currently active subscription:

`az account set --subscription `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subscription_id</span>

- List supported regions for the currently active subscription:

`az account list-locations`

- Print an access token to be used with `MS Graph API`:

`az account get-access-token --resource-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ms-graph</span>

- Print details of the currently active subscription in a specific format:

`az account show --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json|tsv|table|yaml</span>
