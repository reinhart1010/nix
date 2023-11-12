---
layout: page
title: common/loadtest (English)
description: "Run a load test on the selected HTTP or WebSockets URL."
content_hash: 8f6a9d9109ca741868ed792add97a61ae973cd48
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# loadtest

Run a load test on the selected HTTP or WebSockets URL.
More information: <https://github.com/alexfernandez/loadtest>.

- Run with concurrent users and a specified amount of requests per second:

`loadtest --concurrency `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --rps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">200</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Run with a custom HTTP header:

`loadtest --headers "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">accept:text/plain;text-html</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Run with a specific HTTP method:

`loadtest --method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GET</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>
