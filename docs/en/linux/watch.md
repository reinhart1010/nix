---
layout: page
title: linux/watch (English)
description: "Execute a command repeatedly, and monitor the output in full-screen mode."
content_hash: c52c3be0c00bec0904385f56bf90a476b6f0730d
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/watch.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/watch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# watch

Execute a command repeatedly, and monitor the output in full-screen mode.
More information: <https://manned.org/watch>.

- Monitor files in the current directory:

`watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls</span>

- Monitor disk space and highlight the changes:

`watch -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">df</span>

- Monitor "node" processes, refreshing every 3 seconds:

`watch -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ps aux | grep node</span>`"`

- Monitor disk space and if it changes, stop monitoring:

`watch -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">df</span>
