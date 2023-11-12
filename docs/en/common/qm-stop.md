---
layout: page
title: common/qm-stop (English)
description: "Stop a virtual machine."
content_hash: 57a30a4208c0cb0c701d317133ea56aeafb23bb9
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# qm stop

Stop a virtual machine.
More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Stop a virtual machine immediately:

`qm stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VM_ID</span>

- Stop a virtual machine and wait for at most 10 seconds:

`qm stop --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VM_ID</span>

- Stop a virtual machine and skip lock (only root can use this option):

`qm stop --skiplock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VM_ID</span>

- Stop a virtual machine and don't deactivate storage volumes:

`qm stop --keepActive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VM_ID</span>
