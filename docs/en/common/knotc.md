---
layout: page
title: common/knotc (English)
description: "Control knot DNS server."
content_hash: 407569342f66d9b9edbdcc1b3cf17a14f337724f
last_modified_at: 2024-06-26
tldri18n_status: 2
---
# knotc

Control knot DNS server.
More information: <https://www.knot-dns.cz/docs/latest/html/man_knotc.html>.

- Start editing a zone:

`knotc zone-begin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zone</span>

- Set an A record with TTL of 3600:

`knotc zone-set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zone</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subdomain</span>` 3600 A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>

- Finish editing the zone:

`knotc zone-commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zone</span>

- Get the current zone data:

`knotc zone-read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zone</span>

- Get the current server configuration:

`knotc conf-read server`
