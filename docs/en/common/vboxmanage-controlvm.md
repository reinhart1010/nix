---
layout: page
title: common/vboxmanage-controlvm (English)
description: "Change the state and the settings of a currently running virtual machine."
content_hash: 70608c77c6e4e0f1f89d5f7164d0355b6ce79ef3
last_modified_at: 2023-12-06
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/vboxmanage-controlvm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vboxmanage-controlvm

Change the state and the settings of a currently running virtual machine.
More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-controlvm>.

- Temporarily stop the execution of a virtual machine:

`VBoxManage controlvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid|vm_name</span>` pause`

- Resume the execution of a paused virtual machine:

`VBoxManage controlvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid|vm_name</span>` resume`

- Perform a cold reset on the virtual machine:

`VBoxManage controlvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid|vm_name</span>` reset`

- Poweroff a virtual machine with the same effect as pulling the power cable of a computer:

`VBoxManage controlvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid|vm_name</span>` poweroff`

- Shutdown the virtual machine and save its current state:

`VBoxManage controlvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid|vm_name</span>` savestate`

- Send an ACPI (Advanced Configuration and Power Interface) shutdown signal to the virtual machine:

`VBoxManage controlvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid|vm_name</span>` acpipowerbutton`

- Send command to reboot itself to the guest OS:

`VBoxManage controlvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid|vm_name</span>` reboot`

- Shutdown down the virtual machine without saving its state:

`VBoxManage controlvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid|vm_name</span>` shutdown`
