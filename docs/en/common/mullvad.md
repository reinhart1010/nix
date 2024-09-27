---
layout: page
title: common/mullvad (English)
description: "CLI client for Mullvad VPN."
content_hash: c86ef89c5bd303ea44f89cfaf5a550907057cda2
last_modified_at: 2024-09-27
tldri18n_status: 2
---
# mullvad

CLI client for Mullvad VPN.
See also: `fastd`, `ivpn`, `mozillavpn`, `warp-cli`.
More information: <https://mullvad.net/>.

- Link your Mullvad account with the specified account number:

`mullvad account set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">account_number</span>

- Enable LAN access while VPN is on:

`mullvad lan set allow`

- Establish the VPN tunnel:

`mullvad connect`

- Check status of VPN tunnel:

`mullvad status`
