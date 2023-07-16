---
layout: page
title: common/speedtest-cli (English)
description: "Test internet bandwidth using <https://speedtest.net>."
content_hash: 74b03aec679f651c428627b855846a0702eda7c8
last_modified_at: 2023-07-16
---
# speedtest-cli

Test internet bandwidth using <https://speedtest.net>.
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
