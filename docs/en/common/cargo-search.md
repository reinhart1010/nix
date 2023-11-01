---
layout: page
title: common/cargo-search (English)
description: "Search for packages on <https://crates.io>."
content_hash: 7de2104090e43024ef043b20803f0d6596b2d36c
last_modified_at: 2023-11-01
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cargo search

Search for packages on <https://crates.io>.
The crates are displayed along with descriptions in TOML format suitable for copying into `Cargo.toml`.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-search.html>.

- Search for packages:

`cargo search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query</span>

- Show `n` results (default: 10, max: 100):

`cargo search --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query</span>
