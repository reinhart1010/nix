---
layout: page
title: linux/qm-wait (English)
description: "Wait until the virtual machine is stopped."
content_hash: 651bf2dd4a058b3972bc54fa02e06785f65c6892
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# qm wait

Wait until the virtual machine is stopped.
More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Wait until the virtual machine is stopped:

`qm wait `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>

- Wait until the virtual machine is stopped with a 10 second timeout:

`qm wait --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>

- Send a shutdown request, then wait until the virtual machine is stopped with a 10 second timeout:

`qm shutdown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` && qm wait --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>
