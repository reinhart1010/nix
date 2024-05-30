---
layout: page
title: common/virt-qemu-run (English)
description: "Experimental tool to run a QEMU Guest VM independent of `libvirtd`."
content_hash: 0248c7bc007ac4a7ae4c792cc05a205758f86fcf
last_modified_at: 2024-05-30
tldri18n_status: 2
---
# virt-qemu-run

Experimental tool to run a QEMU Guest VM independent of `libvirtd`.
More information: <https://libvirt.org/manpages/virt-qemu-run.html>.

- Run a QEMU virtual machine:

`virt-qemu-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/guest.xml</span>

- Run a QEMU virtual machine and store the state in a specific directory:

`virt-qemu-run --root=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/guest.xml</span>

- Run a QEMU virtual machine and display verbose information about the startup:

`virt-qemu-run --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/guest.xml</span>

- Display help:

`virt-qemu-run --help`
