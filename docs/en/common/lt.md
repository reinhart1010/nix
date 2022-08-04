---
layout: page
title: common/lt (English)
description: "Localtunnel exposes your localhost to the world for easy testing and sharing."
content_hash: bb47726fbbcd5a1e03a2cb7a99844cbf24257a57
---
# lt

Localtunnel exposes your localhost to the world for easy testing and sharing.
More information: <https://github.com/localtunnel/localtunnel>.

- Start tunnel from a specific port:

`lt --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8000</span>

- Specify the upstream server doing the forwarding:

`lt --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8000</span>` --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Request a specific subdomain:

`lt --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8000</span>` --subdomain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subdomain</span>

- Print basic request info:

`lt --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8000</span>` --print-requests`

- Open the tunnel URL in the default web browser:

`lt --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8000</span>` --open`
