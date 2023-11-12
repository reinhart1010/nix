---
layout: page
title: linux/qm-start (English)
description: "Start a virtual machine on QEMU/KVM Virtual Machine Manager."
content_hash: 342e460614b7477f9fc31105c16109ee61597ccc
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/qm-start.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qm start

Start a virtual machine on QEMU/KVM Virtual Machine Manager.
More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Start a specific virtual machine:

`qm start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- Specify the QEMU machine type (i.e. the CPU to emulate):

`qm start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --machine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">q35</span>

- Start a specific virtual machine with a timeout in 60 seconds:

`qm start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60</span>
