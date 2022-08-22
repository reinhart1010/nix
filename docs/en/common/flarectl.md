---
layout: page
title: common/flarectl (English)
description: "Official CLI for Cloudflare."
content_hash: c6d216f97d7cdcb53fa6585882f98244a910e27e
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># flarectl

Official CLI for Cloudflare.
More information: <https://github.com/cloudflare/cloudflare-go/blob/master/cmd/flarectl/README.md>.

- Block a specific IP:

`flarectl firewall rules create --zone="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>`" --value="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>`" --mode="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">block</span>`" --notes="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Block bad actor</span>`"`

- Add a DNS record:

`flarectl dns create --zone="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>`" --name="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app</span>`" --type="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">CNAME</span>`" --content="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">myapp.herokuapp.com</span>`" --proxy`

- List all Cloudflare IPv4/IPv6 ranges:

`flarectl ips --ip-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ipv4|ipv6|all</span>

- Create many new Cloudflare zones automatically with names from `domains.txt`:

`for domain in $(cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domains.txt</span>`); do flarectl zone info --zone=$domain; done`

- List all firewall rules:

`flarectl firewall rules list`
