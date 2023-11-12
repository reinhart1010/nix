---
layout: page
title: common/diskonaut (English)
description: "Terminal disk space navigator, written in Rust."
content_hash: f477402d902ce371922b0d6987045d917f369a22
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# diskonaut

Terminal disk space navigator, written in Rust.
More information: <https://github.com/imsnif/diskonaut>.

- Start `diskonaut` in the current directory:

`diskonaut`

- Start `diskonaut` in a specific directory:

`diskonaut `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Show file sizes rather than their block usage on the disk:

`diskonaut --apparent-size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Disable deletion confirmation:

`diskonaut --disable-delete-confirmation`
