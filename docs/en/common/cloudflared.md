---
layout: page
title: common/cloudflared (English)
description: "Command-line tool to create a persistent connection to the Cloudflare network."
content_hash: de277bd20189084c767c09b5fbf4ec0ab61b3f7c
last_modified_at: 2024-01-25
tldri18n_status: 2
---
# cloudflared

Command-line tool to create a persistent connection to the Cloudflare network.
More information: <https://developers.cloudflare.com/argo-tunnel/>.

- Authenticate and associate the connection to a domain in the Cloudflare account:

`cloudflared tunnel login`

- Create a tunnel with a specific name:

`cloudflared tunnel create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Establish a tunnel to a host in Cloudflare from the local server:

`cloudflared tunnel --hostname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` localhost:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_number</span>

- Establish a tunnel to a host in Cloudflare from the local server, without verifying the local server's certificate:

`cloudflared tunnel --hostname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` localhost:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_number</span>` --no-tls-verify`

- Save logs to a file:

`cloudflared tunnel --hostname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` http://localhost:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_number</span>` --loglevel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">panic|fatal|error|warn|info|debug</span>` --logfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Install cloudflared as a system service:

`cloudflared service install`
