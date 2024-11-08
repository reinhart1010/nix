---
layout: page
title: linux/dhcpcd (한국어)
description: "DHCP 클라이언트."
content_hash: 8fc6440bced1cc56dbf1f8c0f03910dec543866c
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/dhcpcd.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dhcpcd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dhcpcd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dhcpcd

DHCP 클라이언트.
더 많은 정보: <https://roy.marples.name/projects/dhcpcd>.

- 모든 주소 임대 해제:

`sudo dhcpcd --release`

- DHCP 서버에 새 임대 요청:

`sudo dhcpcd --rebind`
