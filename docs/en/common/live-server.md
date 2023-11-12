---
layout: page
title: common/live-server (English)
description: "A simple development HTTP server with live reload capability."
content_hash: 7bb9a5b1d804b6e3a5212ba0c74d54174c5382ca
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# live-server

A simple development HTTP server with live reload capability.
More information: <https://github.com/tapio/live-server>.

- Serve an `index.html` file and reload on changes:

`live-server`

- Specify a port (default is 8080) from which to serve a file:

`live-server --port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8081</span>

- Specify a given file to serve:

`live-server --open=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">about.html</span>

- Proxy all requests for ROUTE to URL:

`live-server --proxy=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http:localhost:3000</span>
