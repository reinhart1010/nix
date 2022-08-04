---
layout: page
title: common/warp-diag (English)
description: "Diagnostic and feedback tool for Cloudflare's WARP service."
content_hash: c39ff32899183f7da2d428321d37888d70c8de7e
related_topics:
  - title: Indonesia version
    url: /id/common/warp-diag.html
    icon: bi bi-globe
---
# warp-diag

Diagnostic and feedback tool for Cloudflare's WARP service.
See also: `warp-cli`.
More information: <https://developers.cloudflare.com/warp-client/>.

- Generate a zip file with information about the system configuration and the WARP connection:

`warp-diag`

- Generate a zip file with debug information including a timestamp to the output filename:

`warp-diag --add-ts`

- Save the output file under a specific directory:

`warp-diag --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Submit a new feedback to Cloudflare's WARP interactively:

`warp-diag feedback`
