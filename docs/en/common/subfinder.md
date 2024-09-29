---
layout: page
title: common/subfinder (English)
description: "Discover valid subdomains for websites."
content_hash: 7f2434f58c4eeef77e6bdc7704748915b3f5ee1d
last_modified_at: 2024-09-29
tldri18n_status: 2
---
# subfinder

Discover valid subdomains for websites.
Designed as a passive framework to be useful for bug bounties and safe for penetration testing.
More information: <https://github.com/projectdiscovery/subfinder>.

- Find subdomains for a specific [d]omain:

`subfinder -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Show only the subdomains found:

`subfinder -silent -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Show only active subdomains:

`subfinder -nW -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Use all sources for enumeration:

`subfinder -all -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Use a given comma-separated list of [r]esolvers:

`subfinder -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8,1.1.1.1,...</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
