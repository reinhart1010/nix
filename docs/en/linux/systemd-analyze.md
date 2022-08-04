---
layout: page
title: linux/systemd-analyze (English)
description: "Analyze and debug system manager."
content_hash: ec970b8a2b676a63cb191758c3793e181a19923e
---
# systemd-analyze

Analyze and debug system manager.
Show timing details about the boot process of units (services, mount points, devices, sockets).
More information: <https://manned.org/systemd-analyze>.

- List time of each unit to start up:

`systemd-analyze blame`

- Print a tree of the time-critical chain of units:

`systemd-analyze critical-chain`

- Create an SVG file showing when each system service started, highlighting the time that they spent on initialization:

`systemd-analyze plot > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.svg</span>

- Plot a dependency graph and convert it to an SVG file:

`systemd-analyze dot | dot -T`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">svg</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.svg</span>

- Show security scores of running units:

`systemd-analyze security`
