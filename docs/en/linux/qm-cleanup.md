---
layout: page
title: linux/qm-cleanup (English)
description: "Clean up resources on QEMU/KVM Virtual Machine Manager like tap devices, VGPUs, etc."
content_hash: 091ca67c5c5d3c48e8f34b6d769f7d60c2283d03
---
# qm cleanup

Clean up resources on QEMU/KVM Virtual Machine Manager like tap devices, VGPUs, etc.
Called after a VM shuts down, crashes, etc.
More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Clean up resources:

`qm cleanup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clean-shutdown</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">guest-requested</span>
