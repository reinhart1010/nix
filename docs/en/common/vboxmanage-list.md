---
layout: page
title: common/vboxmanage-list (English)
description: "List information about the Oracle VM VirtualBox software and associated service."
content_hash: 9eebe35a4e3088e4cd03a066d72a938fd31bb969
last_modified_at: 2023-12-06
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/vboxmanage-list.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vboxmanage-list

List information about the Oracle VM VirtualBox software and associated service.
More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-list>.

- List all VirtualBox virtual machines:

`VBoxManage list vms`

- Show DHCP servers available on the host system:

`VBoxManage list dhcpservers`

- Show Oracle VM VirtualBox extension packs currently installed:

`VBoxManage list extpacks`

- Show all virtual machine groups:

`VBoxManage list groups`

- Show virtual disk settings that are currently in use by VirtualBox:

`VBoxManage list hdds`

- Show host-only network interfaces available on host system:

`VBoxManage list hostonlyifs`

- Show the list of currently running virtual machines:

`VBoxManage list runningvms`

- Show host system information:

`VBoxManage list hostinfo`
