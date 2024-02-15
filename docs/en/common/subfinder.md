---
layout: page
title: common/subfinder (English)
description: "Discover valid subdomains for websites."
content_hash: 2061bfb4d6c9f20fb648154f157751ade93e3200
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# subfinder

Discover valid subdomains for websites.
Designed as a passive framework to be useful for bug bounties and safe for penetration testing.
More information: <https://github.com/projectdiscovery/subfinder>.

- Find subdomains for a specific [d]omain:

`subfinder -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Show only the subdomains found:

`subfinder --silent -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Use a brute-force attack to find subdomains:

`subfinder -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` -b`

- Remove wildcard subdomains:

`subfinder -nW -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Use a given comma-separated list of [r]esolvers:

`subfinder -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8,1.1.1.1,...</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
