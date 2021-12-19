---
layout: page
title: linux/rmmod (English)
description: "Remove modules from the Linux kernel."
content_hash: a87edd88678db0ee7d0874db12ddf6c232ab467a
---
# rmmod

Remove modules from the Linux kernel.
More information: <https://manned.org/rmmod>.

- Remove a module from the kernel:

`sudo rmmob `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Remove a module from the kernel and display verbose information:

`sudo rmmob --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Remove a module from the kernel and send errors to syslog instead of standard error:

`sudo rmmob --syslog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Display help:

`rmmob --help`

- Display version:

`rmmob --version`
