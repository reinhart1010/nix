---
layout: page
title: common/kdig (English)
description: "Advanced DNS lookup utility."
content_hash: 622d2ae7967529b8c0d9d09a9ae446f6ac00e470
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# kdig

Advanced DNS lookup utility.
More information: <https://www.knot-dns.cz/docs/latest/html/man_kdig.html>.

- Lookup the IP(s) associated with a hostname (A records):

`kdig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Specify a specific DNS server to query (e.g. Google DNS):

`kdig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>

- Query a specific DNS record type associated with a given domain name:

`kdig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">A|AAAA|NS|SOA|DNSKEY|ANY</span>

- Lookup the IP(s) associated with a hostname (A records) using DNS over TLS (DoT):

`kdig -d @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>` +tls-ca +tls-host=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dns.google</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Lookup the IP(s) associated with a hostname (A records) using DNS over HTTPS (DoH):

`kdig -d @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.1.1.1</span>` +https +tls-hostname=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1dot1dot1dot1.cloudflare-dns.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
