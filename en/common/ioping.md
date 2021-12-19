---
layout: page
title: common/ioping (English)
description: "Monitor I/O latency in real time."
content_hash: ac3104b41f1d87e1abacfefed404e5235f835702
---
# ioping

Monitor I/O latency in real time.
More information: <https://github.com/koct9i/ioping>.

- Show disk I/O latency using the default values and the current directory:

`ioping .`

- Measure latency on /tmp using 10 requests of 1 megabyte each:

`ioping -c 10 -s 1M /tmp`

- Measure disk seek rate on `/dev/sdX`:

`ioping -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Measure disk sequential speed on `/dev/sdX`:

`ioping -RL `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>
