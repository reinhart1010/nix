---
layout: page
title: common/subfinder (English)
description: "A subdomain discovery tool that discovers valid subdomains for websites."
content_hash: d40da4f0a9bb687d129aae0c17ff44c267e315ff
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# subfinder

A subdomain discovery tool that discovers valid subdomains for websites.
Designed as a passive framework to be useful for bug bounties and safe for penetration testing.
More information: <https://github.com/subfinder/subfinder>.

- Find subdomains for a specific domain:

`subfinder -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Show only the subdomains found:

`subfinder --silent -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Use a brute-force attack to find subdomains:

`subfinder -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` -b`

- Remove wildcard subdomains:

`subfinder -nW -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Use a given comma-separated list of resolvers:

`subfinder -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8,1.1.1.1,...</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
