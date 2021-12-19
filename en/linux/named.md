---
layout: page
title: linux/named (English)
description: "Execute the DNS (Dynamic Name Service) server daemon that converts host names to IP addresses and vice versa."
content_hash: 8297d06744756835a1a11c968483edd516c09feb
---
# named

Execute the DNS (Dynamic Name Service) server daemon that converts host names to IP addresses and vice versa.
More information: <https://manned.org/named>.

- Read the default configuration file `/etc/named.conf`, read any initial data and listen for queries:

`named`

- Read a custom configuration file:

`named -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/named.conf</span>

- Use IPv4 or IPv6 only, even if the host machine is capable of utilising other protocols:

`named `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-4|-6</span>

- Listen for queries on a specific port instead of the default port 53:

`named -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Run the server in the foreground and do not daemonize:

`named -f`
