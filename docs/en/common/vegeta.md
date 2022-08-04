---
layout: page
title: common/vegeta (English)
description: "A command-line utility and a library for HTTP load testing."
content_hash: 7a0634354158fbf9190aacf380b30259433ad10d
---
# vegeta

A command-line utility and a library for HTTP load testing.
See also `ab`.
More information: <https://github.com/tsenart/vegeta>.

- Launch an attack lasting 30 seconds:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GET https://example.com</span>`" | vegeta attack -duration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30s</span>

- Launch an attack on a server with a self-signed HTTPS certificate:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GET https://example.com</span>`" | vegeta attack -insecure -duration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30s</span>

- Launch an attack with a rate of 10 requests per second:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GET https://example.com</span>`" | vegeta attack -duration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30s</span>` -rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Launch an attack and display a report:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GET https://example.com</span>`" | vegeta attack -duration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30s</span>` | vegeta report`

- Launch an attack and plot the results on a graph (latency over time):

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GET https://example.com</span>`" | vegeta attack -duration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30s</span>` | vegeta plot > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/results.html</span>

- Launch an attack against multiple URLs from a file:

`vegeta attack -duration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30s</span>` -targets=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">requests.txt</span>` | vegeta report`
