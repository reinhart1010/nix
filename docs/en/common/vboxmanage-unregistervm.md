---
layout: page
title: common/vboxmanage-unregistervm (English)
description: "Unregister a virtual machine (VM)."
content_hash: b72d5121a8db7935288f35b3b437aa88f8b34420
last_modified_at: 2023-11-30
tldri18n_status: 2
---
# vboxmanage-unregistervm

Unregister a virtual machine (VM).
More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-unregistervm>.

- Unregister an existing VM:

`VBoxManage unregistervm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid|vm_name</span>

- Delete hard disk image files, all saved state files, VM logs, and XML VM machine files:

`VBoxManage unregistervm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid|vm_name</span>` --delete`

- Delete all files from the VM:

`VBoxManage unregistervm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid|vm_name</span>` --delete-all`
