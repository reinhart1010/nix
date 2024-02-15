---
layout: page
title: common/rustfmt (English)
description: "Format Rust source code."
content_hash: ec76be8ef6dc5e8da72a283c236063b091c66f7d
last_modified_at: 2024-02-15
related_topics:
  - title: தமிழ் version
    url: /ta/common/rustfmt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/rustfmt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rustfmt

Format Rust source code.
More information: <https://github.com/rust-lang/rustfmt>.

- Format a file, overwriting the original file in-place:

`rustfmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.rs</span>

- Check a file for formatting and display any changes on the console:

`rustfmt --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.rs</span>

- Backup any modified files before formatting (the original file is renamed with a `.bk` extension):

`rustfmt --backup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.rs</span>
