---
layout: page
title: linux/ntpd (English)
description: "The official NTP (Network Time Protocol) daemon to synchronize the system clock to remote time servers or local reference clocks."
content_hash: e8693e321299b2080713a2c7360446d8b56ff437
last_modified_at: 2024-04-29
tldri18n_status: 2
---
# ntpd

The official NTP (Network Time Protocol) daemon to synchronize the system clock to remote time servers or local reference clocks.
More information: <https://manned.org/ntpd>.

- Start the daemon:

`sudo ntpd`

- Synchronize system time with remote servers a single time (quit after synchronizing):

`sudo ntpd --quit`

- Synchronize a single time allowing "Big" adjustments:

`sudo ntpd --panicgate --quit`
