---
layout: page
title: common/cargo-install (English)
description: "Build and install a Rust binary."
content_hash: 43cdea9bee39e77ae4039a749f525564ffb7d91d
last_modified_at: 2023-11-01
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cargo install

Build and install a Rust binary.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-install.html>.

- Install a package from <https://crates.io> (the version is optional - latest by default):

`cargo install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Install a package from the specified Git repository:

`cargo install --git `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repo_url</span>

- Build from the specified branch/tag/commit when installing from a Git repository:

`cargo install --git `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repo_url</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch|tag|rev</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name|tag|commit_hash</span>

- List all installed packages and their versions:

`cargo install --list`
