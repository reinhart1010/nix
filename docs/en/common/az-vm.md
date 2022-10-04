---
layout: page
title: common/az-vm (English)
description: "Manage virtual machines in Azure."
content_hash: 3b68a6fe18c773ee415583d2c0b7c1855e1e9032
---
# az vm

Manage virtual machines in Azure.
Part of `az`, the command-line client for Microsoft Azure.
More information: <https://learn.microsoft.com/cli/azure/vm>.

- List details of available Virtual Machines:

`az vm list`

- Create an `UbuntuServer 18.04 LTS` Virtual Machine and generate ssh keys:

`az vm create --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rg</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>` --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Canonical:UbuntuServer:18.04-LTS:latest</span>` --admin-user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">azureuser</span>` --generate-ssh-keys`

- Stop a Virtual Machine:

`az vm stop --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rg</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>

- Deallocate a Virtual Machine:

`az vm deallocate --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rg</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>

- Start a Virtual Machine:

`az vm start --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rg</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>

- Restart a Virtual Machine:

`az vm restart --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rg</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>

- List VM images available in the Azure Marketplace:

`az vm image list`
