---
layout: page
title: windows/psping (English)
description: "A ping tool that includes TCP ping, latency and bandwidth measurement."
content_hash: ecc0ed06e10b06e34c7e12bb5a537f8f62868785
---
# psping

A ping tool that includes TCP ping, latency and bandwidth measurement.
More information: <https://learn.microsoft.com/sysinternals/downloads/psping>.

- Ping a host using ICMP:

`psping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>

- Ping a host over a TCP port:

`psping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Specify the number of pings and perform it quietly:

`psping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pings</span>` -q`

- Ping the target over TCP 50 times and produce a histogram of the results:

`psping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` -q -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` -h`

- Display usage information:

`psping /?`
