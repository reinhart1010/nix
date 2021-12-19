---
layout: page
title: common/vzdump (English)
description: "Backup Utility for virtual machines and containers."
content_hash: de36c03bf051bc0d5f93873ca09d831d38289b34
---
# vzdump

Backup Utility for virtual machines and containers.
More information: <https://pve.proxmox.com/pve-docs/vzdump.1.html>.

- Dump a guest virtual machine into the default dump directory (usually `/var/lib/vz/dump/`), excluding snapshots:

`vzdump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>

- Back up the guest virtual machines with the IDs 101, 102, and 103:

`vzdump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">101 102 103</span>

- Dump a guest virtual machine using a specific mode:

`vzdump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suspend|snapshot</span>

- Back up all guest systems and send an notification email to the root and admin users:

`vzdump --all --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suspend</span>` --mailto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">root</span>` --mailto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">admin</span>

- Use snapshot mode (no downtime required) and a non-default dump directory:

`vzdump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` --dumpdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">snapshot</span>

- Back up all guest virtual machines excluding the IDs 101 and 102:

`vzdump --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suspend</span>` --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">101, 102</span>
