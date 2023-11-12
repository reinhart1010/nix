---
layout: page
title: common/cloudflared (English)
description: "Command-line tool to create a persistent connection to the Cloudflare network."
content_hash: 8e3aa0543e6a9f8bbe6d378111b134b5e0732e8c
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# cloudflared

Command-line tool to create a persistent connection to the Cloudflare network.
More information: <https://developers.cloudflare.com/argo-tunnel/>.

- Authenticate and associate the connection to a domain in the Cloudflare account:

`cloudflared tunnel login`

- Establish a tunnel to a host in Cloudflare from the local server:

`cloudflared tunnel --hostname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` localhost:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_number</span>

- Establish a tunnel to a host in Cloudflare from the local server, without verifying the local server's certificate:

`cloudflared tunnel --hostname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` localhost:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_number</span>` --no-tls-verify`

- Save logs to a file:

`cloudflared tunnel --hostname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` http://localhost:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_number</span>` --loglevel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">panic|fatal|error|warn|info|debug</span>` --logfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Install cloudflared as a system service:

`cloudflared service install`
