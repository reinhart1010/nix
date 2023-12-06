---
layout: page
title: common/vboxmanage-showvminfo (English)
description: "Show information about registered virtual machine."
content_hash: bcb2edf5015b210a7ab302e05e500260e94bb9ba
last_modified_at: 2023-12-06
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/vboxmanage-showvminfo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vboxmanage-showvminfo

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
