---
layout: page
title: common/feroxbuster (English)
description: "Simple, fast, recursive content discovery tool written in Rust."
content_hash: dddd4a2470f69511cb2d3fb2a90f4602e8a160af
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# feroxbuster

Simple, fast, recursive content discovery tool written in Rust.
Used to brute-force hidden paths on web servers and more.
More information: <https://epi052.github.io/feroxbuster-docs/docs/>.

- Discover specific directories and files that match in the wordlist with extensions and 100 threads and a random user-agent:

`feroxbuster --url "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>`" --wordlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` --threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --extensions "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">php,txt</span>`" --random-agent`

- Enumerate directories without recursion through a specific proxy:

`feroxbuster --url "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>`" --wordlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` --no-recursion --proxy "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://127.0.0.1:8080</span>`"`

- Find links in webpages:

`feroxbuster --url "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>`" --extract-links`

- Filter by a specific status code and a number of chars:

`feroxbuster --url "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>`" --filter-status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">301</span>` --filter-size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4092</span>
