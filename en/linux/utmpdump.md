---
layout: page
title: linux/utmpdump (English)
description: "Dump and load btmp, utmp and wtmp accounting files."
content_hash: 31e188a9f99aaccd03a1eccf36733e682d7f16d5
---
# utmpdump

Dump and load btmp, utmp and wtmp accounting files.
More information: <https://manned.org/utmpdump>.

- Dump the `/var/log/wtmp` file to the standard output as plain text:

`utmpdump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/var/log/wtmp</span>

- Load a previously dumped file into `/var/log/wtmp`:

`utmpdump -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dumpfile</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/var/log/wtmp</span>
