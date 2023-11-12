---
layout: page
title: common/ngrep (English)
description: "Filter network traffic packets using regular expressions."
content_hash: d044dc712f52c8899c57f4c7ad1c2a1ad04f525a
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# ngrep

Filter network traffic packets using regular expressions.
More information: <https://github.com/jpr5/ngrep>.

- Capture traffic of all interfaces:

`ngrep -d any`

- Capture traffic of a specific interface:

`ngrep -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Capture traffic crossing port 22 of interface eth0:

`ngrep -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22</span>

- Capture traffic from or to a host:

`ngrep host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.example.com</span>

- Filter keyword 'User-Agent:' of interface eth0:

`ngrep -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">User-Agent:</span>`'`
