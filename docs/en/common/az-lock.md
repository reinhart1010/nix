---
layout: page
title: common/az-lock (English)
description: "Manage Azure locks."
content_hash: 0aa80df8e1fea271a1fedb5a13811a0036c984ab
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# az lock

Manage Azure locks.
Part of `azure-cli` (also known as `az`).
More information: <https://learn.microsoft.com/cli/azure/lock>.

- Create a read-only subscription level lock:

`az lock create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lock_name</span>` --lock-type ReadOnly`

- Create a read-only resource group level lock:

`az lock create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lock_name</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>` --lock-type ReadOnly`

- Delete a subscription level lock:

`az lock delete --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lock_name</span>

- Delete a resource group level lock:

`az lock delete --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lock_name</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>

- List out all locks on the subscription level:

`az lock list`

- Show a subscription level lock:

`az lock show -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lock_name</span>
