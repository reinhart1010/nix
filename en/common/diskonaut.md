---
layout: page
title: common/diskonaut (English)
description: "Terminal disk space navigator, written in Rust."
content_hash: 6f17d1016f69e6a99d6c0772ea75a87a73ecec9c
---
# diskonaut

Terminal disk space navigator, written in Rust.
More information: <https://github.com/imsnif/diskonaut>.

- Start diskonaut in the current directory:

`diskonaut`

- Start diskonaut in a specific directory:

`diskonaut `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Show file sizes rather than their block usage on the disk:

`diskonaut --apparent-size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Disable deletion confirmation:

`diskonaut --disable-delete-confirmation`
