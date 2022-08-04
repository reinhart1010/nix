---
layout: page
title: common/drill (English)
description: "Perform various DNS queries."
content_hash: b1997c82fea963823fd48c340dadfe8fe2067381
related_topics:
  - title: italiano version
    url: /it/common/drill.html
    icon: bi bi-globe
---
# drill

Perform various DNS queries.
More information: <https://manned.org/drill>.

- Lookup the IP(s) associated with a hostname (A records):

`drill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Lookup the mail server(s) associated with a given domain name (MX record):

`drill mx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Get all types of records for a given domain name:

`drill any `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Specify an alternate DNS server to query:

`drill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>

- Perform a reverse DNS lookup on an IP address (PTR record):

`drill -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>

- Perform DNSSEC trace from root servers down to a domain name:

`drill -TD `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Show DNSKEY record(s) for a domain name:

`drill -s dnskey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
