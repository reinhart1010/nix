---
layout: page
title: common/runsvdir (English)
description: "Run an entire directory of services."
content_hash: de1765aa8e5ffc7f33e930de581419de1251a139
last_modified_at: 2024-10-08
related_topics:
  - title: 中文 version
    url: /zh/common/runsvdir.html
    icon: bi bi-globe
tldri18n_status: 2
---
# runsvdir

Run an entire directory of services.
More information: <https://manned.org/runsvdir.8>.

- Start and manage all services in a directory as the current user:

`runsvdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/services</span>

- Start and manage all services in a directory as root:

`sudo runsvdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/services</span>

- Start services in separate sessions:

`runsvdir -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/services</span>
