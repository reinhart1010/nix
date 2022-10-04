---
layout: page
title: linux/dnstracer (English)
description: "The dnstracer command determines where a DNS gets its information from."
content_hash: 008bda74ce7d8f6a0e33dd609c4c5c76de8b664a
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dnstracer

The dnstracer command determines where a DNS gets its information from.
More information: <https://manned.org/dnstracer>.

- Find out where your local DNS got the information on www.example.com:

`dnstracer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.example.com</span>

- Start with a [s]pecific DNS that you already know:

`dnstracer -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dns.example.org</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.example.com</span>

- Only query IPv4 servers:

`dnstracer -4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.example.com</span>

- Retry each request 5 times on failure:

`dnstracer -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.example.com</span>

- Display all steps during execution:

`dnstracer -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.example.com</span>

- Display an [o]verview of all received answers after execution:

`dnstracer -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.example.com</span>
