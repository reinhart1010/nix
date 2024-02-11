---
layout: page
title: common/dig (English)
description: "DNS lookup utility."
content_hash: 09adaf1026a5e772f4d677509063b3fe3ad7fd6c
last_modified_at: 2024-02-11
related_topics:
  - title: español version
    url: /es/common/dig.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dig.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/dig.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dig.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/dig.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/dig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dig

DNS lookup utility.
More information: <https://manned.org/dig>.

- Lookup the IP(s) associated with a hostname (A records):

`dig +short `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Get a detailed answer for a given domain (A records):

`dig +noall +answer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Query a specific DNS record type associated with a given domain name:

`dig +short `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">A|MX|TXT|CNAME|NS</span>

- Specify an alternate DNS server to query:

`dig @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Perform a reverse DNS lookup on an IP address (PTR record):

`dig -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>

- Find authoritative name servers for the zone and display SOA records:

`dig +nssearch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Perform iterative queries and display the entire trace path to resolve a domain name:

`dig +trace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Query a DNS server over a non-standard [p]ort using the TCP protocol:

`dig +tcp -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dns_server_ip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
