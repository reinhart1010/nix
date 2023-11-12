---
layout: page
title: common/virsh-domblklist (English)
description: "List information about block devices associated with a virtual machine."
content_hash: 3c8335cc5db6f09694e40d5c2ae96c6e2b6c19fc
last_modified_at: 2023-11-12
related_topics:
  - title: 한국어 version
    url: /ko/common/virsh-domblklist.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/virsh-domblklist.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virsh-domblklist

List information about block devices associated with a virtual machine.
See also: `virsh`.
More information: <https://manned.org/virsh>.

- List the target name and source path of the block devices:

`virsh domblklist --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>

- List the disk type and device value as well as the target name and source path:

`virsh domblklist --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>` --details`
