---
layout: page
title: common/caddy (English)
description: "An enterprise-ready open source web server with automatic HTTPS, written in Go."
content_hash: 2ba98e4e0c630116ea6e58fea766c150757298cd
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/caddy.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/caddy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# caddy

An enterprise-ready open source web server with automatic HTTPS, written in Go.
More information: <https://caddyserver.com>.

- Start Caddy in the foreground:

`caddy run`

- Start Caddy with the specified Caddyfile:

`caddy run --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/Caddyfile</span>

- Start Caddy in the background:

`caddy start`

- Stop a background Caddy process:

`caddy stop`

- Run a simple file server on the specified port with a browsable interface:

`caddy file-server --listen :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8000</span>` --browse`

- Run a reverse proxy server:

`caddy reverse-proxy --from :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` --to localhost:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8000</span>
