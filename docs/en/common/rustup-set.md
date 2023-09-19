---
layout: page
title: common/rustup-set (English)
description: "Alter `rustup` settings."
content_hash: 092a8d17efc8abada5c6bd8da52f7a1955318882
last_modified_at: 2023-09-19
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rustup set

Alter `rustup` settings.
More information: <https://rust-lang.github.io/rustup>.

- Set the default host triple:

`rustup set default-host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_triple</span>

- Set the default profile (`minimal` includes only `rustc`, `rust-std` and `cargo`, whereas `default` adds `rust-docs`, `rustfmt` and `clippy`):

`rustup set profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minimal|default</span>

- Set whether `rustup` should update itself when running `rustup update`:

`rustup set auto-self-update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enable|disable|check-only</span>
