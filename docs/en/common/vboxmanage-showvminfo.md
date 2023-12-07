---
layout: page
title: common/vboxmanage-showvminfo (English)
description: "Show information about registered virtual machine."
content_hash: bcb2edf5015b210a7ab302e05e500260e94bb9ba
last_modified_at: 2023-12-07
tldri18n_status: 2
---
# vboxmanage-showvminfo

Show information about registered virtual machine.
More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-showvminfo>.

- Show information about a particular virtual machine:

`VBoxManage showvminfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name|uuid</span>

- Show more detailed information about a particular virtual machine:

`VBoxManage showvminfo --details `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name|uuid</span>

- Show information in a machine readable format:

`VBoxManage showvminfo --machinereadable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name|uuid</span>

- Specify password ID if the virtual machine is encrypted:

`VBoxManage showvminfo --password-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name|uuid</span>

- Specify the password file if the virtual machine is encrypted:

`VBoxManage showvminfo --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/password_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name|uuid</span>

- Show the logs of a specific virtual machine:

`VBoxManage showvminfo --log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name|uuid</span>
