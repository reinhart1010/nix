---
layout: page
title: linux/ntpd (English)
description: "The official NTP (Network Time Protocol) daemon to synchronize the system clock to remote time servers or local reference clocks."
content_hash: e8693e321299b2080713a2c7360446d8b56ff437
last_modified_at: 2024-04-28
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/ntpd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ntpd

The official NTP (Network Time Protocol) daemon to synchronize the system clock to remote time servers or local reference clocks.
More information: <https://manned.org/ntpd>.

- Start the daemon:

`sudo ntpd`

- Synchronize system time with remote servers a single time (quit after synchronizing):

`sudo ntpd --quit`

- Synchronize a single time allowing "Big" adjustments:

`sudo ntpd --panicgate --quit`
