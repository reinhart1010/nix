---
layout: page
title: common/cargo-verify-project (English)
description: "Check the correctness of the `Cargo.toml` manifest and print the result as a JSON object."
content_hash: 8e25abd39fefcfbefa03d71851acd2c3a3c323ae
last_modified_at: 2023-11-01
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cargo verify-project

Check the correctness of the `Cargo.toml` manifest and print the result as a JSON object.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-verify-project.html>.

- Check the correctness of the current project's manifest:

`cargo verify-project`

- Check the correctness of the specified manifest file:

`cargo verify-project --manifest-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/Cargo.toml</span>
