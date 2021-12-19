---
layout: page
title: common/subfinder (English)
description: "A subdomain discovery tool that discovers valid subdomains for websites."
content_hash: 2070ce2bf560efab1dbdd83304b3d9a3aacb88f5
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

`subfinder -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.1.1.1</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
