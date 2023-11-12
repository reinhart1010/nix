---
layout: page
title: linux/systemd-analyze (English)
description: "Analyze and debug system manager."
content_hash: 7edce1d5550b695f1a508546c27793d2e8361858
last_modified_at: 2023-11-12
related_topics:
  - title: polski version
    url: /pl/linux/systemd-analyze.html
    icon: bi bi-globe
tldri18n_status: 2
---
# systemd-analyze

Analyze and debug system manager.
Show timing details about the boot process of units (services, mount points, devices, sockets).
More information: <https://www.freedesktop.org/software/systemd/man/systemd-analyze.html>.

- List all running units, ordered by the time they took to initialize:

`systemd-analyze blame`

- Print a tree of the time-critical chain of units:

`systemd-analyze critical-chain`

- Create an SVG file showing when each system service started, highlighting the time that they spent on initialization:

`systemd-analyze plot > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.svg</span>

- Plot a dependency graph and convert it to an SVG file:

`systemd-analyze dot | dot -T`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">svg</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.svg</span>

- Show security scores of running units:

`systemd-analyze security`
