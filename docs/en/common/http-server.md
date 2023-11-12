---
layout: page
title: common/http-server (English)
description: "Simple static HTTP server to serve static files."
content_hash: becc1f03c5f96eef8c53420210da8336c49c493a
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# http-server

Simple static HTTP server to serve static files.
More information: <https://github.com/http-party/http-server>.

- Start an HTTP server listening on the default port to serve the current directory:

`http-server`

- Start an HTTP server on a specific port to serve a specific directory:

`http-server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Start an HTTP server using basic authentication:

`http-server --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Start an HTTP server with directory listings disabled:

`http-server -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">false</span>

- Start an HTTPS server on the default port using the specified certificate:

`http-server --ssl --cert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/cert.pem</span>` --key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/key.pem</span>

- Start an HTTP server and include the client's IP address in the output logging:

`http-server --log-ip`

- Start an HTTP server with CORS enabled by including the `Access-Control-Allow-Origin: *` header in all responses:

`http-server --cors`

- Start an HTTP server with logging disabled:

`http-server --silent`
