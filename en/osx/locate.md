---
layout: page
title: osx/locate (English)
description: "Find filenames quickly."
content_hash: f8deb627d76229d084899bb5d3e8574e7f9e7cb9
related_topics:
  - title: 中文 version
    url: /zh/osx/locate.html
    icon: bi bi-globe
---
# locate

Find filenames quickly.
More information: <https://manned.org/locate>.

- Look for pattern in the database. Note: the database is recomputed periodically (usually weekly or daily):

`locate "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>`"`

- Look for a file by its exact filename (a pattern containing no globbing characters is interpreted as `*pattern*`):

`locate */`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Recompute the database. You need to do it if you want to find recently added files:

`sudo /usr/libexec/locate.updatedb`
