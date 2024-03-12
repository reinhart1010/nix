---
layout: page
title: linux/dhcpcd (English)
description: "DHCP client."
content_hash: fc65773cb7aa08880ed099244b2b491aea055625
last_modified_at: 2024-03-12
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dhcpcd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dhcpcd

DHCP client.
More information: <https://roy.marples.name/projects/dhcpcd>.

- Release all address leases:

`sudo dhcpcd --release`

- Request the DHCP server for new leases:

`sudo dhcpcd --rebind`
