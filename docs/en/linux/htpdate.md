---
layout: page
title: linux/htpdate (English)
description: "Synchronize local date and time via HTTP headers from web servers."
content_hash: c1790644feffb1b0f87484f73bc1681927a159ac
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# htpdate

Synchronize local date and time via HTTP headers from web servers.
More information: <https://www.vervest.org/htp/>.

- Synchronize date and time:

`sudo htpdate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Perform simulation of synchronization, without any action:

`htpdate -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Compensate the systematic clock drift:

`sudo htpdate -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Set time immediate after the synchronization:

`sudo htpdate -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>
