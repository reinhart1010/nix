---
layout: page
title: common/dnsx (English)
description: "A fast and multi-purpose DNS toolkit to run multiple DNS queries."
content_hash: 10a95be8d40210c70f3aab4f72f44dee65224923
last_modified_at: 2024-04-14
tldri18n_status: 2
---
# dnsx

A fast and multi-purpose DNS toolkit to run multiple DNS queries.
Note: input to `dnsx` needs to be passed through `stdin` (pipe `|`) in some cases.
See also: `dig`, `dog`, `dnstracer`.
More information: <https://github.com/projectdiscovery/dnsx>.

- Query the A record of a (sub)domain and show [re]sponse received:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` | dnsx -a -re`

- Query all the DNS records (A, AAAA, CNAME, NS, TXT, SRV, PTR, MX, SOA, AXFR, CAA):

`dnsx -recon -re <<< `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Query a specific type of DNS record:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` | dnsx -re -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a|aaaa|cname|ns|txt|srv|ptr|mx|soa|any|axfr|caa</span>

- Output [r]esponse [o]nly (do not show the queried domain or subdomain):

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` | dnsx -ro`

- Display raw response of a query, specifying [r]esolvers to use and retry attempts for failures:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` | dnsx -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">debug|raw</span>` -resolver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.1.1.1,8.8.8.8,...</span>` -retry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>

- Brute force DNS records using a placeholder:

`dnsx -domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FUZZ.example.com</span>` -wordlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/wordlist.txt</span>` -re`

- Brute force DNS records from a list of [d]omains and wordlists, appending [o]utput to a file with [n]o [c]olor codes:

`dnsx -domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/domain.txt</span>` -wordlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/wordlist.txt</span>` -re -output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.txt</span>` -no-color`

- Extract `CNAME` records for the given list of subdomains, with [r]ate [l]imiting DNS queries per second:

`subfinder -silent -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` | dnsx -cname -re -rl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>
