---
layout: page
title: osx/nettop (English)
description: "Display updated information about the network."
content_hash: 4a5c36f58f6764d08198536d61d4b4cf1ff650ff
last_modified_at: 2024-01-31
related_topics:
  - title: español version
    url: /es/osx/nettop.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nettop

Display updated information about the network.
More information: <https://keith.github.io/xcode-man-pages/nettop.1.html>.

- Monitor TCP and UDP sockets from all interfaces:

`nettop`

- Monitor TCP sockets from Loopback interfaces:

`nettop -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">loopback</span>

- Monitor a specific process:

`nettop -p "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_id|process_name</span>`"`

- Display a per-process summary:

`nettop -P`

- Print 10 samples of network information:

`nettop -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Monitor changes every 5 seconds:

`nettop -d -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- While running nettop, list interactive commands:

`h`

- Display help:

`nettop -h`
