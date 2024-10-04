---
layout: page
title: linux/eselect-kernel (English)
description: "An `eselect` module for managing the `/usr/src/linux` symlink."
content_hash: 2f1ebc7e8563116054eae540b80afafa272b6b3f
last_modified_at: 2024-10-04
tldri18n_status: 2
---
# eselect kernel

An `eselect` module for managing the `/usr/src/linux` symlink.
More information: <https://wiki.gentoo.org/wiki/Eselect#Kernel>.

- List available kernel symlink targets with their numbers:

`eselect kernel list`

- Set the `/usr/src/linux` symlink by name or number from the `list` command:

`eselect kernel set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|number</span>

- Show what the current kernel symlink points to:

`eselect kernel show`

- Set the kernel symlink to the currently running kernel:

`eselect kernel update`
