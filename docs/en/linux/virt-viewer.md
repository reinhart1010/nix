---
layout: page
title: linux/virt-viewer (English)
description: "Minimal graphical interface for a virtual machine (VM)."
content_hash: 43a890b4bf648ec2b46555ee86b306b452b7db8d
last_modified_at: 2024-02-05
tldri18n_status: 2
---
# virt-viewer

Minimal graphical interface for a virtual machine (VM).
Note: 'domain' refers to the name, UUID or ID for the existing VMs (See: tldr virsh).
More information: <https://manned.org/virt-viewer>.

- Launch `virt-viewer` with a prompt to select running virtual machines:

`virt-viewer`

- Launch `virt-viewer` for a specific virtual machine by ID, UUID or name:

`virt-viewer "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain</span>`"`

- Wait for a virtual machine to start and automatically reconnect if it shutdown and restarts:

`virt-viewer --reconnect --wait "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain</span>`"`

- Connect to a specific remote virtual machine over TLS:

`virt-viewer --connect "xen//`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain</span>`"`

- Connect to a specific remote virtual machine over SSH:

`virt-viewer --connect "qemu+ssh//`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`/system" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain</span>`"`
