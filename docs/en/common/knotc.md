---
layout: page
title: common/knotc (English)
description: "Control knot DNS server."
content_hash: 407569342f66d9b9edbdcc1b3cf17a14f337724f
last_modified_at: 2024-06-25
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/knotc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># knotc

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
