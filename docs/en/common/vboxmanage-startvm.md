---
layout: page
title: common/vboxmanage-startvm (English)
description: "Start a virtual machine."
content_hash: 3de1079931f0e33194d487373afcae2ab1a421c5
last_modified_at: 2024-10-29
tldri18n_status: 2
---
# vboxmanage-startvm

Start a virtual machine.
More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-startvm>.

- Start a virtual machine:

`VBoxManage startvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name|uuid</span>

- Start a virtual machine with the specified UI mode:

`VBoxManage startvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name|uuid</span>` --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">headless|gui|sdl|separate</span>

- Specify a password file to start an encrypted virtual machine:

`VBoxManage startvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name|uuid</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/password_file</span>

- Specify a password ID to start an encrypted virtual machine:

`VBoxManage startvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name|uuid</span>` --password-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password_id</span>

- Start a virtual machine with an environment variable pair name value:

`VBoxManage startvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name|uuid</span>` --put-env=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>
