---
layout: page
title: linux/avahi-resolve (English)
description: "Translate between host names and IP Addresses."
content_hash: b1354917e0efa42fb94f0776fdd48b64a4d3df51
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# avahi-resolve

Translate between host names and IP Addresses.
More information: <https://www.avahi.org/>.

- Resolve a local service to its IPv4:

`avahi-resolve -4 --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service.local</span>

- Resolve an IP to a hostname, verbosely:

`avahi-resolve --verbose --address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP</span>
