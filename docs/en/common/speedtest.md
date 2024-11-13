---
layout: page
title: common/speedtest (English)
description: "Official command-line interface for testing internet bandwidth using <https://speedtest.net>."
content_hash: 258c86606f843501a2676a489a6b50571d914583
last_modified_at: 2024-11-13
related_topics:
  - title: 한국어 version
    url: /ko/common/speedtest.html
    icon: bi bi-globe
tldri18n_status: 2
---
# speedtest

Official command-line interface for testing internet bandwidth using <https://speedtest.net>.
Note: some platforms link `speedtest` to `speedtest-cli`. If some of the examples in this page don't work, see `speedtest-cli`.
More information: <https://www.speedtest.net/apps/cli>.

- Run a speed test:

`speedtest`

- Run a speed test and specify the unit of the output:

`speedtest --unit=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">auto-decimal-bits|auto-decimal-bytes|auto-binary-bits|auto-binary-bytes</span>

- Run a speed test and specify the output format:

`speedtest --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">human-readable|csv|tsv|json|jsonl|json-pretty</span>

- Run a speed test and specify the number of decimal points to use (0 to 8, defaults to 2):

`speedtest --precision=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">precision</span>

- Run a speed test and print its progress (only available for output format `human-readable` and `json`):

`speedtest --progress=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yes|no</span>

- List all `speedtest.net` servers, sorted by distance:

`speedtest --servers`

- Run a speed test to a specific `speedtest.net` server:

`speedtest --server-id=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_id</span>
