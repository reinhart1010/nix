---
layout: page
title: linux/dnsmap (English)
description: "The dnsmap command scans a domain for common subdomains e.g. smtp.domain.org."
content_hash: 018bf6f51328d2db077d54185e85fdf7751d27ab
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dnsmap

The dnsmap command scans a domain for common subdomains e.g. smtp.domain.org.
More information: <https://github.com/resurrecting-open-source-projects/dnsmap>.

- Scan for subdomains using the internal wordlist:

`dnsmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Specify a list of subdomains to check for:

`dnsmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/wordlist.txt</span>

- Store results to a CSV file:

`dnsmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.csv</span>

- Ignore 2 IPs that are false positives (up to 5 possible):

`dnsmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">123.45.67.89,98.76.54.32</span>
