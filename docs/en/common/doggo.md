---
layout: page
title: common/doggo (English)
description: "DNS client for Humans."
content_hash: a27aa6b0511be6102a5805e1449e8edbeaa27f4d
last_modified_at: 2024-09-25
related_topics:
  - title: español version
    url: /es/common/doggo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# doggo

DNS client for Humans.
Written in Golang.
More information: <https://github.com/mr-karan/doggo>.

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
