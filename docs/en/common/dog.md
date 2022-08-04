---
layout: page
title: common/dog (English)
description: "DNS lookup utility."
content_hash: f6aff06ec1f517699d094b3543107032c2b8c488
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dog

DNS lookup utility.
It has colorful output, supports DNS-over-TLS and DNS-over-HTTPS protocols, and can emit JSON.
More information: <https://dns.lookup.dog>.

- Lookup the IP(s) associated with a hostname (A records):

`dog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Query the MX records type associated with a given domain name:

`dog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` MX`

- Specify a specific DNS server to query (e.g. Cloudflare):

`dog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` MX @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.1.1.1</span>

- Query over TCP rather than UDP:

`dog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` MX @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.1.1.1</span>` --tcp`

- Query the MX records type associated with a given domain name over TCP using explicit arguments:

`dog --query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --type MX --nameserver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.1.1.1</span>` --tcp`

- Lookup the IP(s) associated with a hostname (A records) using DNS over HTTPS (DoH):

`dog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --https @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://cloudflare-dns.com/dns-query</span>
