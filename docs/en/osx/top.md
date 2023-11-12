---
layout: page
title: osx/top (English)
description: "Display dynamic real-time information about running processes."
content_hash: 72c16604e6adef207715936fd6ba96b9fd9e581f
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/osx/top.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/top.html
    icon: bi bi-globe
tldri18n_status: 2
---
# top

Display dynamic real-time information about running processes.
More information: <https://ss64.com/osx/top.html>.

- Start `top`, all options are available in the interface:

`top`

- Start `top` sorting processes by internal memory size (default order - process ID):

`top -o mem`

- Start `top` sorting processes first by CPU, then by running time:

`top -o cpu -O time`

- Start `top` displaying only processes owned by given user:

`top -user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_name</span>

- Get help about interactive commands:

`?`
