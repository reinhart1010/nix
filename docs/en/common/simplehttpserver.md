---
layout: page
title: common/simplehttpserver (English)
description: "A simple HTTP/S server that supports file upload, basic authentication, and YAML rules for custom responses."
content_hash: c8d612ccca7ec6db90022bdb7816358f8d8ccc88
last_modified_at: 2024-02-16
tldri18n_status: 2
---
# simplehttpserver

A simple HTTP/S server that supports file upload, basic authentication, and YAML rules for custom responses.
A Go alternative to Python's `http.server`.
More information: <https://github.com/projectdiscovery/simplehttpserver>.

- Start the HTTP server serving the current directory with verbose output (listen on all interfaces and port 8000 by default):

`simplehttpserver -verbose`

- Start the HTTP server with basic authentication serving a specific path over port 80 on all interfaces:

`sudo simplehttpserver -basic-auth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` -path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/var/www/html</span>` -listen 0.0.0.0:80`

- Start the HTTP server, enabling HTTPS using a self-signed certificate with custom SAN on all interfaces:

`sudo simplehttpserver -https -domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.selfsigned.com</span>` -listen 0.0.0.0:443`

- Start the HTTP server with custom response headers and upload capability:

`simplehttpserver -upload -header '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">X-Powered-By: Go</span>`' -header '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Server: SimpleHTTPServer</span>`'`

- Start the HTTP server with customizable rules in YAML (see documentation for DSL):

`simplehttpserver -rules `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rules.yaml</span>
