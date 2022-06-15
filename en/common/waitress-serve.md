---
layout: page
title: common/waitress-serve (English)
description: "Pure Python WSGI HTTP Server."
content_hash: ad8e2bee1b90d833c9d3f12fd7326b86cba98ffe
---
# waitress-serve

Pure Python WSGI HTTP Server.
More information: <https://github.com/Pylons/waitress>.

- Run a Python web app:

`waitress-serve `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import.path:wsgi_func</span>

- Listen on port 8080 on localhost:

`waitress-serve --listen=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">localhost</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8080</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import.path:wsgi_func</span>

- Start waitress on a Unix socket:

`waitress-serve --unix-socket=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/socket</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import.path:wsgi_func</span>

- Use 4 threads to process requests:

`waitress-serve --threads=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import.path:wsgifunc</span>

- Call a factory method that returns a WSGI object:

`waitress-serve --call `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import.path.wsgi_factory</span>

- Set the URL scheme to HTTPS:

`waitress-serve --url-scheme=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import.path:wsgi_func</span>
