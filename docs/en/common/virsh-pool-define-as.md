---
layout: page
title: common/virsh-pool-define-as (English)
description: "Create a configuration file in `/etc/libvirt/storage` for a persistent virtual machine storage pool from the provided arguments."
content_hash: a57e943f36e85d75cecb2179cfdf9dd2302f8f80
---
# virsh pool-define-as

Create a configuration file in `/etc/libvirt/storage` for a persistent virtual machine storage pool from the provided arguments.
See also: `virsh`, `virsh-pool-build`, `virsh-pool-start`.
More information: <https://manned.org/virsh>.

- Create the configuration file for a storage pool called pool_name using `/var/vms` as the underlying storage system:

`virsh pool-define-as --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pool_name</span>` --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dir</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/var/vms</span>
