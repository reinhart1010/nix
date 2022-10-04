---
layout: page
title: common/az-sshkey (English)
description: "Manage ssh public key with vm."
content_hash: 3722962ad1f934a255bbfaf2e2efb75e3d5af951
---
# az sshkey

Manage ssh public key with vm.
Part of `azure-cli`.
More information: <https://learn.microsoft.com/cli/azure/sshkey>.

- Create a new SSH key:

`az sshkey create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_group</span>

- Upload an existing SSH key:

`az sshkey create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_group</span>` --public-key "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@path/to/key.pub</span>`"`

- List all SSH public keys:

`az sshkey list`

- Show information about an SSH public key:

`az sshkey show --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_group</span>
