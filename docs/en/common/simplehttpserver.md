---
layout: page
title: common/simplehttpserver (English)
description: "A simple HTTP/S server that supports file upload, basic authentication, and YAML rules for custom responses."
content_hash: 5397a88313279fcfffc8746fd6ee612415efd27a
last_modified_at: 2024-02-15
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/simplehttpserver.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># simplehttpserver

A simple HTTP/S server that supports file upload, basic authentication, and YAML rules for custom responses.
A Go alternative to Python's `http.server`.
More information: <https://github.com/projectdiscovery/simplehttpserver>.

- Start the HTTP server serving the current directory with [v]erbose output (listen on all interfaces and port 8000 by default):

`simplehttpserver -verbose`

- Start the HTTP server with [b]asic authentication serving a specific [p]ath over port 80 on all interfaces:

`sudo simplehttpserver -basic-auth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` -path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/var/www/html</span>` -listen 0.0.0.0:80`

- Start the HTTP server, enabling HTTPS using a self-signed certificate with custom SAN on all interfaces:

`sudo simplehttpserver -https -domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.selfsigned.com</span>` -listen 0.0.0.0:443`

- Start the HTTP server with custom response [h]eaders and [u]pload capability:

`simplehttpserver -upload -header '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">X-Powered-By: Go</span>`' -header '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Server: SimpleHTTPServer</span>`'`

- Start the HTTP server with customizable [r]ules in YAML (see documentation for DSL):

`simplehttpserver -rules `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rules.yaml</span>
