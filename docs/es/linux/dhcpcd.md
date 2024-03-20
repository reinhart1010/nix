---
layout: page
title: linux/dhcpcd (español)
description: "Cliente DHCP."
content_hash: 32150c3bf3f3852cd1f19e7b64c1370e726edcb8
last_modified_at: 2024-03-20
related_topics:
  - title: English version
    url: /en/linux/dhcpcd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dhcpcd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dhcpcd

Cliente DHCP.
Más información: <https://roy.marples.name/projects/dhcpcd>.

- Libera todas las direcciones:

`sudo dhcpcd --release`

- Solicita nuevas direcciones al servidor DHCP:

`sudo dhcpcd --rebind`
