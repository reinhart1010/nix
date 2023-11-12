---
layout: page
title: linux/qm-cloud-init (English)
description: "Configure cloudinit settings for virtual machines managed by Proxmox Virtual Environment (PVE)."
content_hash: a82ebc8b7ad79ab8195b71141559aa26636c9b80
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# qm cloud init

Configure cloudinit settings for virtual machines managed by Proxmox Virtual Environment (PVE).
More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Configure cloudinit settings for a specific user and set password for the user:

`qm cloud-init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` -user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` -password=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Configure cloudinit settings for a specific user and set password for the user with a specific SSH key:

`qm cloud-init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` -user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` -password=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` -sshkey=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh_key</span>

- Set the hostname for a specific virtual machine:

`qm cloud-init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` -hostname=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>

- Configure the network interface settings for a specific virtual machine:

`qm cloud-init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` -ipconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ipconfig</span>

- Configure a shell script to execute before `cloud-ini` is run on a virtual machine:

`qm cloud-init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` -pre `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script</span>
