---
layout: page
title: common/eol (English)
description: "Show end-of-life dates (EoLs) for a number of products."
content_hash: 5033fa6adb57cd0f7d0f6ef2885bd4de8a0f5ce1
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# eol

Show end-of-life dates (EoLs) for a number of products.
More information: <https://github.com/hugovk/norwegianblue>.

- List all available products:

`eol`

- Get EoLs of one or more products:

`eol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">product1 product2 ...</span>

- Open the product webpage:

`eol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">product</span>` --web`

- Get EoLs of a one or more products in a specific format:

`eol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">product1 product2 ...</span>` --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html|json|md|markdown|pretty|rst|csv|tsv|yaml</span>

- Get EoLs of one or more products as a single markdown file:

`eol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">product1 product2 ...</span>` --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">markdown</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eol_report.md</span>

- Display help:

`eol --help`
