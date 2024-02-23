---
layout: page
title: linux/dnsrecon (English)
description: "DNS enumeration tool."
content_hash: d00681aa21479c55e925e20a0156f61db83d3f08
last_modified_at: 2024-02-23
tldri18n_status: 2
---
# dnsrecon

DNS enumeration tool.
More information: <https://github.com/darkoperator/dnsrecon>.

- Scan a domain and save the results to an SQLite database:

`dnsrecon --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database.sqlite</span>

- Scan a domain, specifying the nameserver and performing a zone transfer:

`dnsrecon --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --name_server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nameserver.example.com</span>` --type axfr`

- Scan a domain, using a brute-force attack and a dictionary of subdomains and hostnames:

`dnsrecon --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --dictionary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/dictionary.txt</span>` --type brt`

- Scan a domain, performing a reverse lookup of IP ranges from the SPF record and saving the results to a JSON file:

`dnsrecon --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` -s --json`

- Scan a domain, performing a Google enumeration and saving the results to a CSV file:

`dnsrecon --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` -g --csv`

- Scan a domain, performing DNS cache snooping:

`dnsrecon --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --type snoop --name_server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nameserver.example.com</span>` --dictionary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/dictionary.txt</span>

- Scan a domain, performing zone walking:

`dnsrecon --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --type zonewalk`
