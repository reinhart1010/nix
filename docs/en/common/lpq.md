---
layout: page
title: common/lpq (English)
description: "Show printer queue status."
content_hash: 10b823ec5868fe3a76a9e74a0a1a67a50d81e280
last_modified_at: 2023-12-28
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/lpq.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lpq

Show printer queue status.
More information: <https://openprinting.github.io/cups/doc/man-lpq.html>.

- Show the queued jobs of the default destination:

`lpq`

- Show the queued jobs of all printers enforcing encryption:

`lpq -a -E`

- Show the queued jobs in a long format:

`lpq -l`

- Show the queued jobs of a specific printer or class:

`lpq -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination[/instance]</span>

- Show the queued jobs once every n seconds until the queue is empty:

`lpq +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interval</span>
