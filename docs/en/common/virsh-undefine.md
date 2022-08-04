---
layout: page
title: common/virsh-undefine (English)
description: "Delete a virtual machine."
content_hash: 460b107cb7b0e92989bd33809cdf5645679cbd0c
---
# virsh-undefine

Delete a virtual machine.
More information: <https://manned.org/virsh>.

- Delete only the virtual machine configuration file:

`virsh undefine --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>

- Delete the configuration file and all associated storage volumes:

`virsh undefine --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>` --remove-all-storage`

- Delete the configuration file and the specified storage volumes using the target name or the source name (as obtained from the `virsh domblklist` command):

`virsh undefine --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>` --storage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sda,path/to/source</span>
