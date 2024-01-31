---
layout: page
title: osx/locate (English)
description: "Find filenames quickly."
content_hash: e622832403e84f84d0c415719879a5142148b9cc
last_modified_at: 2024-01-31
related_topics:
  - title: 中文 version
    url: /zh/osx/locate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# locate

Find filenames quickly.
More information: <https://keith.github.io/xcode-man-pages/locate.1.html>.

- Look for pattern in the database. Note: the database is recomputed periodically (usually weekly or daily):

`locate "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>`"`

- Look for a file by its exact filename (a pattern containing no globbing characters is interpreted as `*pattern*`):

`locate */`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Recompute the database. You need to do it if you want to find recently added files:

`sudo /usr/libexec/locate.updatedb`
