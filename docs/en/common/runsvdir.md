---
layout: page
title: common/runsvdir (English)
description: "Run an entire directory of services."
content_hash: e758cdf2b0d1ed220dc1994444e109b53b31ecb5
related_topics:
  - title: 中文 version
    url: /zh/common/runsvdir.html
    icon: bi bi-globe
---
# runsvdir

Run an entire directory of services.
More information: <https://manpages.ubuntu.com/manpages/latest/man8/runsvdir.8.html>.

- Start and manage all services in a directory as the current user:

`runsvdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/services</span>

- Start and manage all services in a directory as root:

`sudo runsvdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/services</span>

- Start services in separate sessions:

`runsvdir -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/services</span>
