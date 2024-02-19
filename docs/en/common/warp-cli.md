---
layout: page
title: common/warp-cli (English)
description: "Connect, disconnect and switch modes of a connection to Cloudflare's WARP service."
content_hash: fd6575517c0cc0e8553e76377e684410f78744cf
last_modified_at: 2024-02-19
related_topics:
  - title: Indonesia version
    url: /id/common/warp-cli.html
    icon: bi bi-globe
tldri18n_status: 2
---
# warp-cli

Connect, disconnect and switch modes of a connection to Cloudflare's WARP service.
WARP is a VPN that encrypts traffic for privacy, security, and speed.
See also: `fastd`, `ivpn`, `mozzilavpn`, `mullvad`.
More information: <https://developers.cloudflare.com/warp-client/>.

- Register the current device to WARP (must be run before first connection):

`warp-cli register`

- Connect to WARP:

`warp-cli connect`

- Disconnect from WARP:

`warp-cli disconnect`

- Display the WARP connection status:

`warp-cli status`

- Switch to a specific mode:

`warp-cli set-mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mode</span>

- Display help:

`warp-cli help`

- Display help for a subcommand:

`warp-cli help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>
