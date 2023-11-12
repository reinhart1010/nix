---
layout: page
title: common/virt-clone (English)
description: "Clone a libvirt virtual machine."
content_hash: 536498f606a90ada7c18828fe3e16b82ec02afa6
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# virt-clone

Clone a libvirt virtual machine.
More information: <https://manned.org/virt-clone>.

- Clone a virtual machine and automatically generate a new name, storage path, and MAC address:

`virt-clone --original `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>` --auto-clone`

- Clone a virtual machine and specify the new name, storage path, and MAC address:

`virt-clone --original `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_vm_name</span>` --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/new_storage</span>` --mac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ff:ff:ff:ff:ff:ff|RANDOM</span>
