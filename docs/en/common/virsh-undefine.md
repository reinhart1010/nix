---
layout: page
title: common/virsh-undefine (English)
description: "Delete a virtual machine."
content_hash: 460b107cb7b0e92989bd33809cdf5645679cbd0c
last_modified_at: 2023-11-12
related_topics:
  - title: 한국어 version
    url: /ko/common/virsh-undefine.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/virsh-undefine.html
    icon: bi bi-globe
tldri18n_status: 2
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
