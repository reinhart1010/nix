---
layout: page
title: common/az-network (English)
description: "Manage Azure Network resources."
content_hash: 85e8dd4b58fe23f77853bdcf07ecb88932e8db6e
---
# az network

Manage Azure Network resources.
Part of `azure-cli`.
More information: <https://learn.microsoft.com/cli/azure/network>.

- List network resources in a region that are used against a subscription quota:

`az network list-usages`

- List all virtual networks in a subscription:

`az network vnet list`

- Create a virtual network:

`az network vnet create --address-prefixes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.0/16</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vnet</span>` --resource_group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>` --submet-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subnet</span>` --subnet-prefixes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.0/24</span>

- Enable accelerated networking for a network interface card:

`az network nic update --accelerated-networking true --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nic</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_group</span>
