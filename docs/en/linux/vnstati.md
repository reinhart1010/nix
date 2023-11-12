---
layout: page
title: linux/vnstati (English)
description: "PNG image output support for vnStat."
content_hash: 1e920b5ef944a5687899c71037cd7139ffe14ca5
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# vnstati

PNG image output support for vnStat.
More information: <https://manned.org/vnstati>.

- Output a summary of the last 2: months, days, and all-time:

`vnstati --summary --iface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">network_interface</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.png</span>

- Output the 10 most traffic-intensive days of all time:

`vnstati --top10 --iface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">network_interface</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.png</span>

- Output monthly traffic statistics from the last 12 months:

`vnstati --months --iface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">network_interface</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.png</span>

- Output hourly traffic statistics from the last 24 hours:

`vnstati --hours --iface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">network_interface</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.png</span>
