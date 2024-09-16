---
layout: page
title: common/az-vm (English)
description: "Manage virtual machines in Azure."
content_hash: 6e405031e353d296247282d680be6116fab284a2
last_modified_at: 2024-09-16
related_topics:
  - title: español version
    url: /es/common/az-vm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# az vm

Manage virtual machines in Azure.
Part of `azure-cli` (also known as `az`).
More information: <https://learn.microsoft.com/cli/azure/vm>.

- Display a table of available Virtual Machines:

`az vm list --output table`

- Create a virtual machine using the default Ubuntu image and generate SSH keys:

`az vm create --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rg</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>` --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UbuntuLTS</span>` --admin-user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">azureuser</span>` --generate-ssh-keys`

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
