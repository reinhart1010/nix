---
layout: page
title: common/warp-diag (English)
description: "Diagnostic and feedback tool for Cloudflare's WARP service."
content_hash: 72c1a6211fa36add66663cf2e404c8dafa5d3174
last_modified_at: 2024-03-14
related_topics:
  - title: Indonesia version
    url: /id/common/warp-diag.html
    icon: bi bi-globe
tldri18n_status: 2
---
# warp-diag

Diagnostic and feedback tool for Cloudflare's WARP service.
See also: `warp-cli`.
More information: <https://developers.cloudflare.com/warp-client/>.

- Generate a Zip file with information about the system configuration and the WARP connection:

`warp-diag`

- Generate a Zip file with debug information including a timestamp to the output filename:

`warp-diag --add-ts`

- Save the output file under a specific directory:

`warp-diag --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Submit a new feedback to Cloudflare's WARP interactively:

`warp-diag feedback`
