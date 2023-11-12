---
layout: page
title: common/az-sshkey (English)
description: "Manage ssh public keys with virtual machines."
content_hash: b1e0145a2aadad129ead0865a456b54027dbbc31
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/az-sshkey.html
    icon: bi bi-globe
tldri18n_status: 2
---
# az sshkey

Manage ssh public keys with virtual machines.
Part of `azure-cli` (also known as `az`).
More information: <https://learn.microsoft.com/cli/azure/sshkey>.

- Create a new SSH key:

`az sshkey create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_group</span>

- Upload an existing SSH key:

`az sshkey create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_group</span>` --public-key "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@path/to/key.pub</span>`"`

- List all SSH public keys:

`az sshkey list`

- Show information about an SSH public key:

`az sshkey show --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_group</span>
