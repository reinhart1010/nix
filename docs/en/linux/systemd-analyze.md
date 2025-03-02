---
layout: page
title: linux/systemd-analyze (English)
description: "Analyze and debug system manager."
content_hash: 80d89aa20bcd3a3d142379d38b614f18ac009c02
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/linux/systemd-analyze.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/systemd-analyze.html
    icon: bi bi-globe
tldri18n_status: 2
---
# systemd-analyze

Analyze and debug system manager.
Show timing details about the boot process of units (services, mount points, devices, sockets).
More information: <https://www.freedesktop.org/software/systemd/man/systemd-analyze.html>.

- Print the last system startup time:

`systemd-analyze`

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
