---
layout: page
title: common/lychee (English)
description: "Find broken URLs."
content_hash: cdc7a5cc987980d3db8301a1ce594bf131d8283f
last_modified_at: 2024-09-20
tldri18n_status: 2
---
# lychee

Find broken URLs.
More information: <https://lychee.cli.rs/usage/cli/>.

- Scan a website for broken links:

`lychee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Display a breakdown of error types:

`lychee --format detailed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Limit the amount of connections to prevent DDOS protection:

`lychee --max-concurrency `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">links.txt</span>

- Check files in a directory structure for any broken URLs:

`grep -r "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>`" | lychee -`

- Display help:

`lychee --help`
