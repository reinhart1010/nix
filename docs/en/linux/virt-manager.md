---
layout: page
title: linux/virt-manager (English)
description: "CLI launcher for virt-manager, a desktop user interface for managing KVM and Xen virtual machines and LXC containers."
content_hash: dab2544bd2719c89edb8d3c616097fecc842f51b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# virt-manager

CLI launcher for virt-manager, a desktop user interface for managing KVM and Xen virtual machines and LXC containers.
More information: <https://manpages.ubuntu.com/manpages/man1/virt-manager.1.html>.

- Launch virt-manager:

`virt-manager`

- Connect to a hypervisor:

`virt-manager --connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hypervisor_uri</span>

- Don't fork virt-manager process into background on startup:

`virt-manager --no-fork`

- Print debug output:

`virt-manager --debug`

- Open the "New VM" wizard:

`virt-manager --show-domain-creator`

- Show domain details window:

`virt-manager --show-domain-editor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|id|uuid</span>

- Show domain performance window:

`virt-manager --show-domain-performance `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|id|uuid</span>

- Show connection details window:

`virt-manager --show-host-summary`
