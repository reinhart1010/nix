---
layout: page
title: common/siege (English)
description: "HTTP loadtesting and benchmarking tool."
content_hash: 2de2a264fa7d1a1744cb3e48144bf724a4d57cec
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# siege

HTTP loadtesting and benchmarking tool.
More information: <https://www.joedog.org/siege-manual/>.

- Test a URL with default settings:

`siege `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Test a list of URLs:

`siege --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/url_list.txt</span>

- Test list of URLs in a random order (Simulates internet traffic):

`siege --internet --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/url_list.txt</span>

- Benchmark a list of URLs (without waiting between requests):

`siege --benchmark --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/url_list.txt</span>

- Set the amount of concurrent connections:

`siege --concurrent=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/url_list.txt</span>

- Set how long for the siege to run for:

`siege --time=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30s</span>` --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/url_list.txt</span>
