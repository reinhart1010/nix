---
layout: page
title: common/warp-cli (English)
description: "Connect, disconnect and switch modes of a connection to Cloudflare's WARP service."
content_hash: 60dcfe3d3fcb7be2716d900151ff91adef4fd7b9
last_modified_at: 2024-10-16
related_topics:
  - title: Indonesia version
    url: /id/common/warp-cli.html
    icon: bi bi-globe
tldri18n_status: 2
---
# warp-cli

Connect, disconnect and switch modes of a connection to Cloudflare's WARP service.
WARP is a VPN that encrypts traffic for privacy, security, and speed.
See also: `fastd`, `ivpn`, `mozillavpn`, `mullvad`.
More information: <https://developers.cloudflare.com/warp-client/>.

- Register the current device to WARP (must be run before first connection):

`warp-cli registration new`

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
