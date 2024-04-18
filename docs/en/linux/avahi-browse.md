---
layout: page
title: linux/avahi-browse (English)
description: "Display services and hosts exposed on the local network via mDNS/DNS-SD."
content_hash: 0586f77d829a7fa49a4f6351894b9ce78df36965
last_modified_at: 2024-04-18
related_topics:
  - title: 中文 version
    url: /zh/linux/avahi-browse.html
    icon: bi bi-globe
tldri18n_status: 2
---
# avahi-browse

Display services and hosts exposed on the local network via mDNS/DNS-SD.
Avahi is compatible with Bonjour (Zeroconf) found in Apple devices.
More information: <https://www.avahi.org/>.

- List services available on the local network along with their addresses and ports, ignoring ones on the local machine:

`avahi-browse --all --resolve --ignore-local`

- Quickly list services in the local network in SSV format for scripts:

`avahi-browse --all --terminate --parsable`

- List domains in the neighbourhood:

`avahi-browse --browse-domains`

- Limit the search to a particular domain:

`avahi-browse --all --domain=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain</span>
