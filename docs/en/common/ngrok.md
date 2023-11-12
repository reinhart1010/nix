---
layout: page
title: common/ngrok (English)
description: "Reverse proxy that creates a secure tunnel from a public endpoint to a locally running web service."
content_hash: 9a9db95761c0524060a641a36e85eba822656ee2
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/ngrok.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ngrok

Reverse proxy that creates a secure tunnel from a public endpoint to a locally running web service.
More information: <https://ngrok.com>.

- Expose a local HTTP service on a given port:

`ngrok http `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>

- Expose a local HTTP service on a specific host:

`ngrok http `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo.dev</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>

- Expose a local HTTPS server:

`ngrok http https://localhost`

- Expose TCP traffic on a given port:

`ngrok tcp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22</span>

- Expose TLS traffic for a specific host and port:

`ngrok tls -hostname=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">443</span>
