---
layout: page
title: linux/sysctl (English)
description: "List and change kernel runtime variables."
content_hash: 93399767f086e9fc924ac4cc090a7f02d0352453
related_topics:
  - title: Deutsch version
    url: /de/linux/sysctl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/sysctl.html
    icon: bi bi-globe
---
# sysctl

List and change kernel runtime variables.

- Show all available variables and their values:

`sysctl -a`

- Set a changeable kernel state variable:

`sysctl -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">section.tunable</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Get currently open file handlers:

`sysctl fs.file-nr`

- Get limit for simultaneous open files:

`sysctl fs.file-max`

- Apply changes from `/etc/sysctl.conf`:

`sysctl -p`
