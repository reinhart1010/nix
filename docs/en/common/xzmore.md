---
layout: page
title: common/xzmore (English)
description: "Display text from `xz` or `lzma` compressed files."
content_hash: ac1e51f769653d18e6faf8426869074a4e5de813
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# xzmore

Display text from `xz` or `lzma` compressed files.
Almost equivalent to `xzless`, except it respects the `PAGER` environment variable, uses `more` by default and you cannot pass options to the pager.
More information: <https://manned.org/xzmore>.

- View a compressed file:

`xzmore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
