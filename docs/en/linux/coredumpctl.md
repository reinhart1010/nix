---
layout: page
title: linux/coredumpctl (English)
description: "Retrieve and process saved core dumps and metadata."
content_hash: 54d7a4e32aa46f17dc70343d65feaf06b924a444
last_modified_at: 2024-12-31
related_topics:
  - title: català version
    url: /ca/linux/coredumpctl.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/coredumpctl.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/coredumpctl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/coredumpctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# coredumpctl

Retrieve and process saved core dumps and metadata.
More information: <https://www.freedesktop.org/software/systemd/man/coredumpctl.html>.

- List all captured core dumps:

`coredumpctl`

- List captured core dumps for a program:

`coredumpctl list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Show information about the core dumps matching a program with `PID`:

`coredumpctl info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- Invoke debugger using the last core dump:

`coredumpctl debug`

- Invoke debugger using the last core dump of a program:

`coredumpctl debug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Extract the last core dump of a program to a file:

`coredumpctl --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` dump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>
