---
layout: page
title: linux/virt-manager (English)
description: "A desktop user interface for managing KVM and Xen virtual machines and LXC containers."
content_hash: bb2dd539bc88f08f5a97bf3ea239b6e0cf7b9828
last_modified_at: 2024-10-08
tldri18n_status: 2
---
# virt-manager

A desktop user interface for managing KVM and Xen virtual machines and LXC containers.
More information: <https://manned.org/virt-manager.1>.

- Launch the GUI:

`virt-manager`

- Connect to a hypervisor:

`virt-manager --connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hypervisor_uri</span>

- Don't fork virt-manager process into background on startup:

`virt-manager --no-fork`

- Print debug output:

`virt-manager --debug`

- Open the "New VM" wizard:

`virt-manager --show-domain-creator`

- Show domain details window for a specific virtual machine/container:

`virt-manager --show-domain-editor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|id|uuid</span>

- Show domain performance window for a specific virtual machine/container:

`virt-manager --show-domain-performance `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|id|uuid</span>

- Show connection details window:

`virt-manager --show-host-summary`
