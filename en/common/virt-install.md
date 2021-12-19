---
layout: page
title: common/virt-install (English)
description: "Create virtual machines with libvirt and begin OS installation."
content_hash: 55e1de544078f4c8523d12f33e020d5580fbb0f3
---
# virt-install

Create virtual machines with libvirt and begin OS installation.
More information: <https://virt-manager.org/>.

- Create a virtual machine with 1 GiB RAM and 12 GiB storage and start Debian installation:

`virt-install --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>` --memory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1024</span>` --disk path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.qcow2</span>`,size=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">12</span>` --cdrom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/debian.iso</span>
