---
layout: page
title: linux/rmmod (English)
description: "Remove modules from the Linux kernel."
content_hash: 576f3929c8da2bb5370590e4a1fc1c3acb0372dd
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/linux/rmmod.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/rmmod.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rmmod

Remove modules from the Linux kernel.
See also: `kmod`, for other module management commands.
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
