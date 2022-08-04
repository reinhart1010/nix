---
layout: page
title: linux/htpdate (English)
description: "Synchronize local date and time via HTTP headers from web servers."
content_hash: f20258de320b428bcda21d33a31394b080d69894
---
# htpdate

Synchronize local date and time via HTTP headers from web servers.
More information: <http://www.vervest.org/htp/>.

- Synchronize date and time:

`sudo htpdate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Perform simulation of synchronization, without any action:

`htpdate -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Compensate the systematic clock drift:

`sudo htpdate -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Set time immediate after the synchronization:

`sudo htpdate -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>
