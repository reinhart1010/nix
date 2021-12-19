---
layout: page
title: common/live-server (English)
description: "A simple development HTTP server with live reload capability."
content_hash: 492ba5efb71e0115d283232da1919fcb49b57fc5
---
# live-server

A simple development HTTP server with live reload capability.
More information: <https://www.npmjs.com/package/live-server>.

- Serve an `index.html` file and reload on changes:

`live-server`

- Specify a port (default is 8080) from which to serve a file:

`live-server --port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8081</span>

- Specify a given file to serve:

`live-server --open=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">about.html</span>

- Proxy all requests for ROUTE to URL:

`live-server --proxy=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http:localhost:3000</span>
