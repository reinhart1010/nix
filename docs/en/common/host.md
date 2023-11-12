---
layout: page
title: common/host (English)
description: "Lookup Domain Name Server."
content_hash: a5bb9d0348fbe5b2149a7fbb9d6bd213e7b99bbe
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# host

Lookup Domain Name Server.
More information: <https://manned.org/host>.

- Lookup A, AAAA, and MX records of a domain:

`host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain</span>

- Lookup a field (CNAME, TXT,...) of a domain:

`host -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">field</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain</span>

- Reverse lookup an IP:

`host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>

- Specify an alternate DNS server to query:

`host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>
