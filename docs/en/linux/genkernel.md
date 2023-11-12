---
layout: page
title: linux/genkernel (English)
description: "Gentoo Linux utility to compile and install kernels."
content_hash: a98c1c7241294712d224bc35db179f1f53f9b3c0
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# genkernel

Gentoo Linux utility to compile and install kernels.
More information: <https://wiki.gentoo.org/wiki/Genkernel>.

- Automatically compile and install a generic kernel:

`sudo genkernel all`

- Build and install the bzImage|initramfs|kernel|ramdisk only:

`sudo genkernel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bzImage|initramfs|kernel|ramdisk</span>

- Apply changes to the kernel configuration before compiling and installing:

`sudo genkernel --menuconfig all`

- Generate a kernel with a custom name:

`sudo genkernel --kernname=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">custom_name</span>` all`

- Use a kernel source outside the default directory `/usr/src/linux`:

`sudo genkernel --kerneldir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` all`
