---
layout: page
title: linux/avahi-browse (English)
description: "Displays services and hosts exposed on the local network via mDNS/DNS-SD."
content_hash: 0bb961303cea0423374422dafaf7844e06e61545
related_topics:
  - title: 中文 version
    url: /zh/linux/avahi-browse.html
    icon: bi bi-globe
---
# avahi-browse

Displays services and hosts exposed on the local network via mDNS/DNS-SD.
Avahi is compatible with Bonjour (Zeroconf) found in Apple devices.
More information: <https://www.avahi.org/>.

- List all services available on the local network along with their addresses and ports while ignoring local ones:

`avahi-browse --all --resolve --ignore-local`

- List all domains:

`avahi-browse --browse-domains`

- Limit the search to a particular domain:

`avahi-browse --all --domain=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain</span>
