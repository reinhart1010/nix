---
layout: page
title: common/virsh-domblklist (English)
description: "List information about block devices associated with a virtual machine."
content_hash: 3c8335cc5db6f09694e40d5c2ae96c6e2b6c19fc
---
# virsh-domblklist

List information about block devices associated with a virtual machine.
See also: `virsh`.
More information: <https://manned.org/virsh>.

- List the target name and source path of the block devices:

`virsh domblklist --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>

- List the disk type and device value as well as the target name and source path:

`virsh domblklist --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>` --details`
