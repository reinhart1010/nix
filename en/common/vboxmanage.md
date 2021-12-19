---
layout: page
title: common/vboxmanage (English)
description: "Command-line interface to VirtualBox."
content_hash: 92098b90cf14c5fa11ca71623f33624cb3da5787
---
# VBoxManage

Command-line interface to VirtualBox.
Includes all the functionality of the GUI and more.
More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-intro>.

- List all VirtualBox virtual machines:

`VBoxManage list vms`

- Show information about a particular virtual machine:

`VBoxManage showvminfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|uuid</span>

- Start a virtual machine:

`VBoxManage startvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|uuid</span>

- Start a virtual machine in headless mode:

`VBoxManage startvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|uuid</span>` -type headless`

- Shutdown the virtual machine and save its current state:

`VBoxManage controlvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|uuid</span>` savestate`

- Shutdown down the virtual machine without saving its state:

`VBoxManage controlvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|uuid</span>` poweroff`

- Update VBox extension packs:

`VBoxManage extpack install --replace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VboxExtensionPackFileName</span>
