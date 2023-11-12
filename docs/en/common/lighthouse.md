---
layout: page
title: common/lighthouse (English)
description: "Analyzes web applications and web pages, collecting modern performance metrics and insights on developer best practices."
content_hash: 52fe1c50bffb804174169e1d105ac29ac6565d5a
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# lighthouse

Analyzes web applications and web pages, collecting modern performance metrics and insights on developer best practices.
More information: <https://github.com/GoogleChrome/lighthouse>.

- Generate an HTML report for a specific website and save it to a file in the current directory:

`lighthouse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Generate a JSON report and print it:

`lighthouse --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Generate a JSON report and save it to a specific file:

`lighthouse --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json</span>` --output-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Generate a report using the browser in headless mode without logging to `stdout`:

`lighthouse --quiet --chrome-flags="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--headless</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Generate a report, using the HTTP header key/value pairs in the specified JSON file for all requests:

`lighthouse --extra-headers=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Generate a report for specific categories only:

`lighthouse --only-categories=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">performance,accessibility,best-practices,seo,pwa</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Generate a report with device emulation and all throttling disabled:

`lighthouse --screenEmulation.disabled --throttling-method=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">provided</span>` --no-emulatedUserAgent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Display help:

`lighthouse --help`
