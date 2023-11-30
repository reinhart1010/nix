---
layout: page
title: common/vboxmanage-createvm (English)
description: "Create a new virtual machine."
content_hash: 3810cf6ed48560ca8074823f6db33ea6197c0489
last_modified_at: 2023-11-30
tldri18n_status: 2
---
# vboxmanage-createvm

Create a new virtual machine.
More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-createvm>.

- Create a new VM with default settings:

`VBoxManage createvm --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>

- Set the base folder where the VM configuration will be stored:

`VBoxManage createvm --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>` --basefolder `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Set the guest OS type (one of `VBoxManage list ostypes`) for the imported VM:

`VBoxManage createvm --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>` --ostype `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ostype</span>

- Register the created VM in VirtualBox:

`VBoxManage createvm --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>` --register`

- Set the VM to the specified groups:

`VBoxManage createvm --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>` --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group1,group2,...</span>

- Set the Universally Unique Identifier (UUID) of the VM:

`VBoxManage createvm --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>` --uuid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid</span>

- Set the cipher to use for encryption:

`VBoxManage createvm --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>` --cipher `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AES-128|AES-256</span>
