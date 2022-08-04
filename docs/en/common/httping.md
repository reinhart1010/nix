---
layout: page
title: common/httping (English)
description: "Measure the latency and throughput of a web server."
content_hash: a58d060cac673fbee47e1ddb1d92290f70397a02
---
# httping

Measure the latency and throughput of a web server.
More information: <https://manned.org/httping>.

- Ping the specified URL:

`httping -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Ping the web server on `host` and `port`:

`httping -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Ping the web server on `host` using a TLS connection:

`httping -l -g https://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ping the web server on `host` using HTTP basic authentication:

`httping -g http://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>
