---
layout: page
title: common/sublist3r (English)
description: "Fast subdomains enumeration tool for penetration testers."
content_hash: 4cdd5578a0ba59f15d5dbf2bc4adc626ed04a974
last_modified_at: 2024-01-30
tldri18n_status: 2
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

- Display help:

`sublist3r --help`
