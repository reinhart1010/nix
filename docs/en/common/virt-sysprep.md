---
layout: page
title: common/virt-sysprep (English)
description: "Reset, unconfigure, or customize a virtual machine image."
content_hash: a6d2a1de3ae481a2f3c0c121790c1592e00df977
---
# virt-sysprep

Reset, unconfigure, or customize a virtual machine image.
More information: <https://manned.org/virt-sysprep>.

- List all supported operations (enabled operations are indicated with asterisks):

`virt-sysprep --list-operations`

- Run all enabled operations but don't actually apply the changes:

`virt-sysprep --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>` --dry-run`

- Run only the specified operations:

`virt-sysprep --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>` --operations `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">operation1,operation2,...</span>

- Generate a new `/etc/machine-id` file and enable customizations to be able to change the host name to avoid network conflicts:

`virt-sysprep --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>` --enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">customizations</span>` --hostname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_name</span>` --operation `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">machine-id</span>
