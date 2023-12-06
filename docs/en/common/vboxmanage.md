---
layout: page
title: common/vboxmanage (English)
description: "Command-line interface to VirtualBox."
content_hash: 584765a891f2f3cc21e888bcb7ff47f35ccff392
last_modified_at: 2023-12-06
tldri18n_status: 2
---
# VBoxManage

Command-line interface to VirtualBox.
Includes all the functionality of the GUI and more.
Some subcommands such as `vboxmanage startvm` have their own usage documentation.
More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-intro>.

- Display version:

`VBoxManage --version`

- Display help:

`VBoxManage --help`

- Display help for a VBoxManage subcommand (like `starvm`, `clonevm`, `import`, `export`, etc.):

`VBoxManage --help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>

- Execute a VboxManage subcommand:

`VBoxManage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>
