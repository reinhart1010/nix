---
layout: page
title: linux/utmpdump (English)
description: "Dump and load btmp, utmp and wtmp accounting files."
content_hash: 071a82fe09d4c4f9a64a49e4851591f78d9dd3b6
---
# utmpdump

Dump and load btmp, utmp and wtmp accounting files.

- Dump the `/var/log/wtmp` file to the standard output as plain text:

`utmpdump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/var/log/wtmp</span>

- Load a previously dumped file into `/var/log/wtmp`:

`utmpdump -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dumpfile</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/var/log/wtmp</span>
