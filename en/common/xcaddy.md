---
layout: page
title: common/xcaddy (English)
description: "The custom build tool for the Caddy Web Server."
content_hash: 71c1adbe922ef93d1d464f17c96be81288cc5847
---
# xcaddy

The custom build tool for the Caddy Web Server.
More information: <https://github.com/caddyserver/xcaddy>.

- Build Caddy server from source:

`xcaddy build`

- Build Caddy server with a specific version (defaults to latest):

`xcaddy build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Build Caddy with a specific module:

`xcaddy build --with `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Build Caddy and output to a specific file:

`xcaddy build --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Build and run Caddy for a development plugin in the current directory:

`xcaddy run`

- Build and run Caddy for a development plugin using a specific Caddy config:

`xcaddy run --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
