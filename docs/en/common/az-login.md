---
layout: page
title: common/az-login (English)
description: "Log in to Azure."
content_hash: c55abd8a02976a1298db5a78a16c5462fbbf98bb
last_modified_at: 2024-10-24
related_topics:
  - title: Deutsch version
    url: /de/common/az-login.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/az-login.html
    icon: bi bi-globe
tldri18n_status: 2
---
# az login

Log in to Azure.
Part of `azure-cli` (also known as `az`).
More information: <https://learn.microsoft.com/cli/azure/reference-index#az-login>.

- Log in interactively:

`az login`

- Log in with a service principal using a client secret:

`az login --service-principal --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://azure-cli-service-principal</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret</span>` --tenant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">someone.onmicrosoft.com</span>

- Log in with a service principal using a client certificate:

`az login --service-principal --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://azure-cli-service-principal</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/cert.pem</span>` --tenant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">someone.onmicrosoft.com</span>

- Log in using a VM's system assigned identity:

`az login --identity`

- Log in using a VM's user assigned identity:

`az login --identity --username /subscriptions/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subscription_id</span>`/resourcegroups/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_rg</span>`/providers/Microsoft.ManagedIdentity/userAssignedIdentities/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_id</span>
