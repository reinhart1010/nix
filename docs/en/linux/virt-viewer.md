---
layout: page
title: linux/virt-viewer (English)
description: "Minimal graphical interface for a virtual machine (VM)."
content_hash: 202573fefbb138801c1382d27dccad3d2e0e8a89
last_modified_at: 2022-12-01
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># virt-viewer

Minimal graphical interface for a virtual machine (VM).
NOTE: 'domain' refers to the name, UUID or ID for the existing VMs (See: tldr virsh).
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
