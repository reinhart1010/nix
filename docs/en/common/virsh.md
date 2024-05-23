---
layout: page
title: common/virsh (English)
description: "Manage virsh guest domains. (Note: 'guest_id' can be the ID, name or UUID of the guest)."
content_hash: 6bd1859b5e257d1fb0985525de5336cd00c6f361
last_modified_at: 2024-05-23
related_topics:
  - title: 한국어 version
    url: /ko/common/virsh.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/virsh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virsh

Manage virsh guest domains. (Note: 'guest_id' can be the ID, name or UUID of the guest).
Some subcommands such as `virsh list` have their own usage documentation.
More information: <https://libvirt.org/manpages/virsh.html>.

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
