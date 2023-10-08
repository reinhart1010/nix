---
layout: page
title: common/cargo-fetch (English)
description: "Fetch dependencies of a package from the network."
content_hash: 80948e20e9c7f6b567ad6672b89838eefd8e5213
last_modified_at: 2023-10-08
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cargo fetch

Fetch dependencies of a package from the network.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-fetch.html>.

- Fetch dependencies from the `Cargo.lock` file:

`cargo fetch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">options</span>

- Display verbose output:

`cargo fetch --verbose`

- Do not print Cargo log messages:

`cargo fetch --quiet`

- Control colored output:

`cargo fetch --color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">auto|always|never</span>

- Path to `Cargo.toml`:

`cargo fetch --manifest-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path</span>

- Prevent Cargo from accessing the network:

`cargo fetch --offline`

- Display help:

`cargo fetch --help`
