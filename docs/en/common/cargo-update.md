---
layout: page
title: common/cargo-update (English)
description: "Update dependencies as recorded in `Cargo.lock`."
content_hash: 5aab54adee6eeafc8a48046621f23d18b8cc2b33
last_modified_at: 2023-09-23
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cargo update

Update dependencies as recorded in `Cargo.lock`.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-update.html>.

- Update dependencies in `Cargo.lock` to the latest possible version:

`cargo update`

- Display what would be updated, but don't actually write the lockfile:

`cargo update --dry-run`

- Update only the specified dependencies:

`cargo update --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependency1</span>` --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependency2</span>` --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependency3</span>

- Set a specific dependency to a specific version:

`cargo update --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependency</span>` --precise `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.3</span>
