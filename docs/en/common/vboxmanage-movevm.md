---
layout: page
title: common/vboxmanage-movevm (English)
description: "Move a virtual machine (VM) to a new location on the host system."
content_hash: 4143eaf3aef35f3932e87bc209471b65303fb507
last_modified_at: 2023-12-23
tldri18n_status: 2
---
# vboxmanage movevm

Move a virtual machine (VM) to a new location on the host system.
More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-movevm>.

- Move the specified virtual machine to the current location:

`VBoxManage movevm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>

- Specify the new location (full or relative pathname) of the virtual machine:

`VBoxManage movevm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>` --folder `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/new_location</span>
