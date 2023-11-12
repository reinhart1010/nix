---
layout: page
title: linux/mpstat (English)
description: "Report CPU statistics."
content_hash: 1761376ee1df9d2c6309f28b6eb458c872b801ca
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# mpstat

Report CPU statistics.
More information: <https://manned.org/mpstat>.

- Display CPU statistics every 2 seconds:

`mpstat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- Display 5 reports, one by one, at 2 second intervals:

`mpstat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- Display 5 reports, one by one, from a given processor, at 2 second intervals:

`mpstat -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>
