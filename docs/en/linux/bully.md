---
layout: page
title: linux/bully (English)
description: "Brute-force the WPS pin of a wireless access point."
content_hash: 6f115363bc127a8f1f2d5e03dfde8924e321d760
last_modified_at: 2022-12-01
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># bully

Brute-force the WPS pin of a wireless access point.
Necessary information must be gathered with `airmon-ng` and `airodump-ng` before using `bully`.
More information: <https://salsa.debian.org/pkg-security-team/bully>.

- Crack the password:

`bully --bssid "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac</span>`" --channel "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">channel</span>`" --bruteforce "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>`"`

- Display help:

`bully --help`
