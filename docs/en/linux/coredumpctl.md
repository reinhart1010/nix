---
layout: page
title: linux/coredumpctl (English)
description: "Retrieve and process saved core dumps and metadata."
content_hash: 0e953cb60aea103e12806389d7edd1aca6bc6274
related_topics:
  - title: español version
    url: /es/linux/coredumpctl.html
    icon: bi bi-globe
---
# coredumpctl

Retrieve and process saved core dumps and metadata.
More information: <https://www.freedesktop.org/software/systemd/man/coredumpctl.html>.

- List all captured core dumps:

`coredumpctl list`

- List captured core dumps for a program:

`coredumpctl list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Show information about the core dumps matching a program with `PID`:

`coredumpctl info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- Invoke debugger using the last core dump of a program:

`coredumpctl debug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Extract the last core dump of a program to a file:

`coredumpctl --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` dump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>
