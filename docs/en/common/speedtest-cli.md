---
layout: page
title: common/speedtest-cli (English)
description: "Test internet bandwidth using <https://speedtest.net>."
content_hash: 0302ca9008504fdc3060d80df3b985a16995f7fa
last_modified_at: 2024-11-13
related_topics:
  - title: 한국어 version
    url: /ko/common/speedtest-cli.html
    icon: bi bi-globe
tldri18n_status: 2
---
# speedtest-cli

Test internet bandwidth using <https://speedtest.net>.
See also: `speedtest` for the official CLI.
More information: <https://github.com/sivel/speedtest-cli>.

- Run a speed test:

`speedtest-cli`

- Run a speed test and display values in bytes, instead of bits:

`speedtest-cli --bytes`

- Run a speed test using `HTTPS`, instead of `HTTP`:

`speedtest-cli --secure`

- Run a speed test without performing download tests:

`speedtest-cli --no-download`

- Run a speed test and generate an image of the results:

`speedtest-cli --share`

- List all `speedtest.net` servers, sorted by distance:

`speedtest-cli --list`

- Run a speed test to a specific speedtest.net server:

`speedtest-cli --server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_id</span>

- Run a speed test and display the results as JSON (suppresses progress information):

`speedtest-cli --json`
