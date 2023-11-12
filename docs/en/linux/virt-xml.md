---
layout: page
title: linux/virt-xml (English)
description: "Edit libvirt Domain XML files with explicit command-line options."
content_hash: 2bbaa513bdee3c43e5fc916f85bc67f66e54b003
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# virt-xml

Edit libvirt Domain XML files with explicit command-line options.
NOTE: 'domain' refers to the name, UUID or ID for the existing VMs (See: tldr virsh).
More information: <https://github.com/virt-manager/virt-manager/blob/main/man/virt-xml.rst>.

- List all the suboptions for a specific option:

`virt-xml --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">option</span>`=?`

- List all the suboptions for disk, network, and boot:

`virt-xml --disk=? --network=? --boot=?`

- Edit a value for a specific domain:

`virt-xml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain</span>` --edit --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">option</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suboption</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_value</span>

- Change the description for a specific domain:

`virt-xml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain</span>` --edit --metadata description="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_description</span>`"`

- Enable/Disable the boot device menu for a specific domain:

`virt-xml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain</span>` --edit --boot bootmenu=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Attach host USB hub to a running VM (See: tldr lsusb):

`virt-xml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain</span>` --update --add-device --hostdev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bus</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device</span>
