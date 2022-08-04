---
layout: page
title: common/openconnect (English)
description: "A VPN client, for Cisco AnyConnect VPNs and others."
content_hash: 73440fee16322c378325bb97e8584be246b03e1b
---
# openconnect

A VPN client, for Cisco AnyConnect VPNs and others.
More information: <https://www.infradead.org/openconnect/manual.html>.

- Connect to a server:

`openconnect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vpn.example.org</span>

- Connect to a server, forking into the background:

`openconnect --background `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vpn.example.org</span>

- Terminate the connection that is running in the background:

`killall -SIGINT openconnect`

- Connect to a server, reading options from a config file:

`openconnect --config=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vpn.example.org</span>

- Connect to a server and authenticate with a specific SSL client certificate:

`openconnect --certificate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vpn.example.org</span>
