---
layout: page
title: osx/nettop (English)
description: "Display updated information about the network."
content_hash: 243b17117711b5eb5d4982429f22fb795ce8b55d
---
# nettop

Display updated information about the network.

- Monitor TCP and UDP sockets from all interfaces:

`nettop`

- Monitor TCP sockets from Loopback interfaces:

`nettop -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">loopback</span>

- Monitor a specific process:

`nettop -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_id|process_name</span>

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
