---
layout: page
title: linux/getconf (English)
description: "Get configuration values from your Linux system."
content_hash: e2a1faec0f699974e12f9d3def1a9f02e3dbf02c
last_modified_at: 2023-01-11
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># getconf

Get configuration values from your Linux system.
More information: <https://manned.org/getconf.1>.

- List [a]ll configuration values available:

`getconf -a`

- List the configuration values for a specific directory:

`getconf -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Check if your linux system is a 32-bit or 64-bit:

`getconf LONG_BIT`

- Check how many processes the current user can run at once:

`getconf CHILD_MAX`

- List every configuration value and then find patterns with the grep command (i.e every value with MAX in it):

`getconf -a | grep MAX`
