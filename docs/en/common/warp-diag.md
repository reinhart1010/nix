---
layout: page
title: common/warp-diag (English)
description: "Diagnostic and feedback tool for Cloudflare's WARP service."
content_hash: 8f75795e79abf809cd5d01b1cad5f2a996a19567
last_modified_at: 2024-01-30
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

- Generate a `zip` file with information about the system configuration and the WARP connection:

`warp-diag`

- Generate a `zip` file with debug information including a timestamp to the output filename:

`warp-diag --add-ts`

- Save the output file under a specific directory:

`warp-diag --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Submit a new feedback to Cloudflare's WARP interactively:

`warp-diag feedback`
