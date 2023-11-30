---
layout: page
title: common/vboxmanage-registervm (English)
description: "Register a virtual machine (VM)."
content_hash: 14633e1e468c4a5b569ae3acfca5584339a6e6cf
last_modified_at: 2023-11-30
tldri18n_status: 2
---
# vboxmanage-registervm

Register a virtual machine (VM).
More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-registervm>.

- Register an existing VM:

`VBoxManage registervm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filename.vbox</span>

- Supply the encryption password file of the VM:

`VBoxManage registervm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filename.vbox</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/password_file</span>

- Prompt for the encryption password on the command line:

`VBoxManage registervm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filename.vbox</span>` --password -`
