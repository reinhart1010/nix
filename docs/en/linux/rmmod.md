---
layout: page
title: linux/rmmod (English)
description: "Remove modules from the Linux kernel."
content_hash: 68cd8ae63a82ca95c543ed2901250d84f2b7b003
last_modified_at: 2023-08-09
---
# rmmod

Remove modules from the Linux kernel.
More information: <https://manned.org/rmmod>.

- Remove a module from the kernel:

`sudo rmmod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Remove a module from the kernel and display verbose information:

`sudo rmmod --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Remove a module from the kernel and send errors to syslog instead of `stderr`:

`sudo rmmod --syslog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Display help:

`rmmod --help`

- Display version:

`rmmod --version`
