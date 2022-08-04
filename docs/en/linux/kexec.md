---
layout: page
title: linux/kexec (English)
description: "Directly reboot into a new kernel."
content_hash: b76ecec45e2ee7b443240848b8ab26e591cb4c8a
---
# kexec

Directly reboot into a new kernel.
More information: <https://manned.org/kexec>.

- Load a new kernel:

`kexec -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/kernel</span>` --initrd=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/initrd</span>` --command-line=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arguments</span>

- Load a new kernel with current boot parameters:

`kexec -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/kernel</span>` --initrd=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/initrd</span>` --reuse-cmdline`

- Execute a currently loaded kernel:

`kexec -e`

- Unload current kexec target kernel:

`kexec -u`
