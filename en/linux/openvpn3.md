---
layout: page
title: linux/openvpn3 (English)
description: "OpenVPN 3 Linux client."
content_hash: 4a237dd5f23cfad3559ef9c3462f1c1bf941b125
---
# openvpn3

OpenVPN 3 Linux client.
More information: <https://community.openvpn.net/openvpn/wiki/OpenVPN3Linux>.

- Start a new VPN session:

`openvpn3 session-start --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.conf</span>

- List established sessions:

`openvpn3 sessions-list`

- Disconnect the currently established session started with given configuration:

`openvpn3 session-manage --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.conf</span>` --disconnect`

- Import VPN configuration:

`openvpn3 config-import --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.conf</span>

- List imported configurations:

`openvpn3 configs-list`
