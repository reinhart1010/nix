---
layout: page
title: common/gau (English)
description: "Get All URLs: fetch known URLs from AlienVault's Open Threat Exchange, the Wayback Machine, and Common Crawl for any domains."
content_hash: 63fcc350e9cb57ba37a131a1b9644af8768d1eb2
last_modified_at: 2024-03-12
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gau.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gau

Get All URLs: fetch known URLs from AlienVault's Open Threat Exchange, the Wayback Machine, and Common Crawl for any domains.
More information: <https://github.com/lc/gau>.

- Fetch all URLs of a domain from AlienVault's Open Threat Exchange, the Wayback Machine, Common Crawl, and URLScan:

`gau `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Fetch URLs of multiple domains:

`gau `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain1 domain2 ...</span>

- Fetch all URLs of several domains from an input file, running multiple threads:

`gau --threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/domains.txt</span>

- Write [o]utput results to a file:

`gau `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/found_urls.txt</span>

- Search for URLs from only one specific provider:

`gau --providers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wayback|commoncrawl|otx|urlscan</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Search for URLs from multiple providers:

`gau --providers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wayback,otx,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Search for URLs within specific date range:

`gau --from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYYMM</span>` --to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYYMM</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
