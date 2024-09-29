---
layout: page
title: common/netdiscover (English)
description: "Network scanner used to find live hosts on a network."
content_hash: 534ad71a241e63892a872c297c9d970f0240f267
last_modified_at: 2024-09-29
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/netdiscover.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># netdiscover

Network scanner used to find live hosts on a network.
More information: <https://github.com/netdiscover-scanner/netdiscover>.

- Scan the IP range on the network interface for active hosts:

`netdiscover -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">172.16.6.0/23</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ens244</span>
