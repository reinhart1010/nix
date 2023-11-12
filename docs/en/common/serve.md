---
layout: page
title: common/serve (English)
description: "Static file serving and directory listing."
content_hash: bac7dba2b8d25bc0fb54040f2e72a61bc7782ab2
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# serve

Static file serving and directory listing.
More information: <https://github.com/vercel/serve>.

- Start an HTTP server listening on the default port to serve the current directory:

`serve`

- Start an HTTP server on a specific [p]ort to serve a specific directory:

`serve -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Start an HTTP server with CORS enabled by including the `Access-Control-Allow-Origin: *` header in all responses:

`serve --cors`

- Start an HTTP server on the default port rewriting all not-found requests to the `index.html` file:

`serve --single`

- Start an HTTPS server on the default port using the specified certificate:

`serve --ssl-cert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/cert.pem</span>` --ssl-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/key.pem</span>

- Start an HTTP server on the default port using a specific configuration file:

`serve --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/serve.json</span>

- Display help:

`serve --help`
