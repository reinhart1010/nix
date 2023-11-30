---
layout: page
title: common/vboxmanage-clonevm (English)
description: "Create a clone of an existing virtual machine (VM)."
content_hash: 60e1bdc7cc13ff768ab20732cd201bac67463e2f
last_modified_at: 2023-11-30
tldri18n_status: 2
---
# vboxmanage-clonevm

Create a clone of an existing virtual machine (VM).
More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-clonevm>.

- Clone the specified VM:

`VBoxManage clonevm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>

- Specify a new name for the new VM:

`VBoxManage clonevm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_vm_name</span>

- Indicate the folder where the new VM configuration is saved:

`VBoxManage clonevm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>` --basefolder `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Register the cloned VM in VirtualBox:

`VBoxManage clonevm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>` --register`
