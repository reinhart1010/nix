---
layout: page
title: common/rustfmt (English)
description: "Tool for formatting Rust source code."
content_hash: 0214776a87539a713caba92e3773025f8bfee872
related_topics:
  - title: 中文 version
    url: /zh/common/rustfmt.html
    icon: bi bi-globe
---
# rustfmt

Tool for formatting Rust source code.
More information: <https://github.com/rust-lang/rustfmt>.

- Format a file, overwriting the original file in-place:

`rustfmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.rs</span>

- Check a file for formatting and display any changes on the console:

`rustfmt --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.rs</span>

- Backup any modified files before formatting (the original file is renamed with a `.bk` extension):

`rustfmt --backup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.rs</span>
