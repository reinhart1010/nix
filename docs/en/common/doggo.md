---
layout: page
title: common/doggo (English)
description: "DNS client for Humans."
content_hash: 1822a2f52baf0fb60bd744f3e979582088dfbccf
last_modified_at: 2024-07-15
tldri18n_status: 2
---
# doggo

DNS client for Humans.
Written in Golang.
More information: <https://doggo.mrkaran.dev>.

- Perform a simple DNS lookup:

`doggo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Query MX records using a specific nameserver:

`doggo MX `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">codeberg.org</span>` @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.1.1.2</span>

- Use DNS over HTTPS:

`doggo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://dns.quad9.net/dns-query</span>

- Output in the JSON format:

`doggo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --json | jq '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.responses[0].answers[].address</span>`'`

- Perform a reverse DNS lookup:

`doggo --reverse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.4.4</span>` --short`
