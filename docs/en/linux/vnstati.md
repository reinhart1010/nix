---
layout: page
title: linux/vnstati (English)
description: "PNG image output support for vnStat."
content_hash: 41e36c41fe8940b1ebf86ea3e1f8995e694208dd
last_modified_at: 2024-05-13
tldri18n_status: 2
---
# vnstati

PNG image output support for vnStat.
More information: <https://manned.org/vnstati>.

- Output a summary of the last 2: months, days, and all-time:

`vnstati --summary --iface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">network_interface</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.png</span>

- Output the 10 most traffic-intensive days of all time:

`vnstati --top 10 --iface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">network_interface</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.png</span>

- Output monthly traffic statistics from the last 12 months:

`vnstati --months --iface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">network_interface</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.png</span>

- Output hourly traffic statistics from the last 24 hours:

`vnstati --hours --iface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">network_interface</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.png</span>
