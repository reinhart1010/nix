---
layout: page
title: common/openconnect (English)
description: "A VPN client, for Cisco AnyConnect VPNs and others."
content_hash: 717dd6be07798765ca369c571986e9511582b5e1
last_modified_at: 2024-01-25
tldri18n_status: 2
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

- Connect to a server, reading options from a configuration file:

`openconnect --config=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vpn.example.org</span>

- Connect to a server and authenticate with a specific SSL client certificate:

`openconnect --certificate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vpn.example.org</span>
