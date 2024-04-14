---
layout: page
title: common/katana (English)
description: "A fast crawler focused on execution in automation pipelines offering both headless and non-headless crawling."
content_hash: 6b171c90be301e2137d0d4a911c2bfcae07394b7
last_modified_at: 2024-04-14
tldri18n_status: 2
---
# katana

A fast crawler focused on execution in automation pipelines offering both headless and non-headless crawling.
See also: `gau`, `scrapy`, `waymore`.
More information: <https://github.com/projectdiscovery/katana>.

- Crawl a list of URLs:

`katana -list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com,https://google.com,...</span>

- Crawl a [u]RL using headless mode using Chromium:

`katana -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>` -headless`

- Use `subfinder` to find subdomains, and then use [p]a[s]sive sources (Wayback Machine, Common Crawl, and AlienVault) for URL discovery:

`subfinder -list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/domains.txt</span>` | katana -passive`

- Pass requests through a proxy (http/socks5) and use custom [H]eaders from a file:

`katana -proxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://127.0.0.1:8080</span>` -headers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/headers.txt</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Specify the crawling [s]trategy, [d]epth of subdirectories to crawl, and rate limiting (requests per second):

`katana -strategy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">depth-first|breadth-first</span>` -depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>` -rate-limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Find subdomains using `subfinder`, crawl each for a maximum number of seconds, and write results to an [o]utput file:

`subfinder -list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/domains.txt</span>` | katana -crawl-duration `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>` -output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.txt</span>
