---
layout: page
title: common/virsh (English)
description: "Manage virsh guest domains. (NOTE: 'guest_id' can be the id, name or UUID of the guest)."
content_hash: 1977ced82b2ebee2ce04bc577fe4f925afe3a7c8
---
# virsh

Manage virsh guest domains. (NOTE: 'guest_id' can be the id, name or UUID of the guest).
Some subcommands such as `virsh list` have their own usage documentation.
More information: <https://libvirt.org/virshcmdref.html>.

- Connect to a hypervisor session:

`virsh connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">qemu:///system</span>

- List all domains:

`virsh list --all`

- Dump guest configuration file:

`virsh dumpxml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">guest_id</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/guest.xml</span>

- Create a guest from a configuration file:

`virsh create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config_file.xml</span>

- Edit a guest's configuration file (editor can be changed with $EDITOR):

`virsh edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">guest_id</span>

- Start/reboot/shutdown/suspend/resume a guest:

`virsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">guest_id</span>

- Save the current state of a guest to a file:

`virsh save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">guest_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Delete a running guest:

`virsh destroy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">guest_id</span>` && virsh undefine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">guest_id</span>
