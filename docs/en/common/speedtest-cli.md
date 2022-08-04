---
layout: page
title: common/speedtest-cli (English)
description: "Unofficial command-line interface for testing internet bandwidth using https://speedtest.net."
content_hash: a30bdf0aac7fb21aba74445b5d0e037b3836d6de
---
# speedtest-cli

Unofficial command-line interface for testing internet bandwidth using https://speedtest.net.
See also `speedtest` for the official CLI.
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
