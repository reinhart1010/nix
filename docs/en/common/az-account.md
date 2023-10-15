---
layout: page
title: common/az-account (English)
description: "Manage Azure subscription information."
content_hash: 40133499814a1bb2bb1494711998f046e61b46ed
last_modified_at: 2023-10-15
related_topics:
  - title: español version
    url: /es/common/az-account.html
    icon: bi bi-globe
---
# az account

Manage Azure subscription information.
Part of `azure-cli` (also known as `az`).
More information: <https://learn.microsoft.com/cli/azure/account>.

- Print a list of subscriptions for the logged in account:

`az account list`

- Set a `subscription` to be the currently active subscription:

`az account set --subscription `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subscription_id</span>

- List supported regions for the currently active subscription:

`az account list-locations`

- Print an access token to be used with `MS Graph API`:

`az account get-access-token --resource-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ms-graph</span>

- Print details of the currently active subscription in a specific format:

`az account show --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json|tsv|table|yaml</span>
