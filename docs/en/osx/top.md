---
layout: page
title: osx/top (English)
description: "Display dynamic real-time information about running processes."
content_hash: 535ba2911ece0c1d8b34be2e69c6f03a663d6d13
related_topics:
  - title: 中文 version
    url: /zh/osx/top.html
    icon: bi bi-globe
---
# top

Display dynamic real-time information about running processes.
More information: <https://ss64.com/osx/top.html>.

- Start top, all options are available in the interface:

`top`

- Start top sorting processes by internal memory size (default order - process ID):

`top -o mem`

- Start top sorting processes first by CPU, then by running time:

`top -o cpu -O time`

- Start top displaying only processes owned by given user:

`top -user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_name</span>

- Get help about interactive commands:

`?`
