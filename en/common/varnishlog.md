---
layout: page
title: common/varnishlog (English)
description: "Display Varnish logs."
content_hash: 116024ad7a0cea0a15da9a6bda06cfd0d0887036
---
# varnishlog

Display Varnish logs.
More information: <https://varnish-cache.org/docs/trunk/reference/varnishlog.html>.

- Display logs in real time:

`varnishlog`

- Only display requests to a specific domain:

`varnishlog -q 'ReqHeader eq "Host: `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>`"'`

- Only display POST requests:

`varnishlog -q 'ReqMethod eq "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">POST</span>`"'`

- Only display requests to a specific path:

`varnishlog -q 'ReqURL eq "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path</span>`"'`

- Only display requests to paths matching a regular expression:

`varnishlog -q 'ReqURL ~ "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regex</span>`"'`
