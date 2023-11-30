---
layout: page
title: common/vboxmanage-import (English)
description: "Import a previously exported virtual machine (VM)."
content_hash: 684cab6435a5403f22ee348e526743b0db0a1780
last_modified_at: 2023-11-30
tldri18n_status: 2
---
# vboxmanage-import

Import a previously exported virtual machine (VM).
More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-import>.

- Import a VM from an OVF or OVA file:

`VBoxManage import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ovf</span>

- Set the name of the imported VM:

`VBoxManage import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ovf</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>

- Indicate the folder where the configuration of the imported VM will be stored:

`VBoxManage import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ovf</span>` --basefolder `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Register the imported VM in VirtualBox:

`VBoxManage import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ovf</span>` --register`

- Perform a dry run to check the import without actually importing:

`VBoxManage import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ovf</span>` --dry-run`

- Set the guest OS type (one of `VBoxManage list ostypes`) for the imported VM:

`VBoxManage import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ovf</span>` --ostype=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ostype</span>

- Set the memory (in megabytes) for the imported VM:

`VBoxManage import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ovf</span>` --memory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Set the number of CPUs for the imported VM:

`VBoxManage import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ovf</span>` --cpus=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>
