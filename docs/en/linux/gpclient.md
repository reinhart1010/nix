---
layout: page
title: linux/gpclient (English)
description: "Connect to a GlobalProtect VPN on Linux via OpenConnect."
content_hash: 28014b62494e571f039f17559dbb47161297f360
last_modified_at: 2024-10-09
tldri18n_status: 2
---
# gpclient

Connect to a GlobalProtect VPN on Linux via OpenConnect.
More information: <https://github.com/yuezk/GlobalProtect-openconnect>.

- Connect to a GlobalProtect VPN using a portal server:

`gpclient connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vpn_gateway_url</span>

- Disconnect from the currently connected VPN server:

`gpclient disconnect`

- Launch the graphical user interface (GUI) for VPN management:

`gpclient launch-gui`

- Use OpenSSL workaround to bypass legacy renegotiation errors:

`gpclient connect --fix-openssl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vpn_gateway_url</span>

- Ignore TLS errors during connection:

`gpclient connect --ignore-tls-errors `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vpn_gateway_url</span>

- Display version:

`gpclient --version`

- Display help for any command:

`gpclient help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
