---
layout: page
title: linux/goldeneye.py (English)
description: "A HTTP DoS test tool."
content_hash: 0f13e5d3afd133e3825dd16f3bec0d46b583deba
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># goldeneye.py

A HTTP DoS test tool.
More information: <https://github.com/jseidl/GoldenEye>.

- Test a specific website:

`./goldeneye.py `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Test a specific website with 100 user agents and 200 concurrent sockets:

`./goldeneye.py `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --useragents 100 --sockets 200`

- Test a specific website without verifying the SSL certificate:

`./goldeneye.py `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --nosslcheck`

- Test a specific website in debug mode:

`./goldeneye.py `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --debug`

- Display help:

`./goldeneye.py --help`
