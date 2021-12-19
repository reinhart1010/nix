---
layout: page
title: common/sublist3r (English)
description: "Fast subdomains enumeration tool for penetration testers."
content_hash: 983b56b6d92d085b54ff59c60bd9103ceef2a2c2
---
# sublist3r

Fast subdomains enumeration tool for penetration testers.
More information: <https://github.com/aboul3la/Sublist3r>.

- Find subdomains for a domain:

`sublist3r --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_name</span>

- Find subdomains for a domain, also enabling brute force search:

`sublist3r --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_name</span>` --bruteforce`

- Save the found subdomains to a text file:

`sublist3r --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_name</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Output all available options:

`sublist3r --help`
