---
layout: page
title: common/limactl (English)
description: "Virtual machine manager for Linux guests, with multiple VM templates available."
content_hash: 2db0583bb5b8f33a8b1aa51d8187f633fb9626e2
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# limactl

Virtual machine manager for Linux guests, with multiple VM templates available.
Can be used to run containers on macOS, but also for generic virtual machine use cases on macOS and Linux hosts.
More information: <https://github.com/lima-vm/lima>.

- List VMs:

`limactl list`

- Create a VM using the default settings and optionally provide a name and/or a template (see `limactl create --list-templates` for available templates):

`limactl create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>` template://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">debian|fedora|ubuntu|…</span>

- Start a VM (this might install some dependencies in it and take a few minutes):

`limactl start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>

- Open a remote shell inside a VM:

`limactl shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>

- Run a command inside a VM:

`limactl shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Stop/shutdown a VM:

`limactl stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>

- Delete a VM:

`limactl remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>
