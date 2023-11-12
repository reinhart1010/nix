---
layout: page
title: linux/utmpdump (English)
description: "Dump and load btmp, utmp and wtmp accounting files."
content_hash: 2daa9d3075a6c12144f2982849e8bb2c9cc1d170
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# utmpdump

Dump and load btmp, utmp and wtmp accounting files.
More information: <https://manned.org/utmpdump>.

- Dump the `/var/log/wtmp` file to `stdout` as plain text:

`utmpdump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/var/log/wtmp</span>

- Load a previously dumped file into `/var/log/wtmp`:

`utmpdump -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dumpfile</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/var/log/wtmp</span>
