---
layout: page
title: common/cargo-yank (English)
description: "Remove a pushed crate from the index. This should only be used when you accidentally release a significantly broken crate."
content_hash: 0a366101b3b3b0fb7a46b69cefb15eedcb089f9d
last_modified_at: 2023-10-31
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cargo yank

Remove a pushed crate from the index. This should only be used when you accidentally release a significantly broken crate.
Note: this does not remove any data. The crate is still present after a yank - this just prevents new projects from using it.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-yank.html>.

- Yank the specified version of a crate:

`cargo yank `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">crate</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Undo a yank (i.e. allow downloading it again):

`cargo yank --undo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">crate</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Specify the name of the registry to use (registry names can be defined in the config - the default is <https://crates.io>):

`cargo yank --registry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">crate</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>
