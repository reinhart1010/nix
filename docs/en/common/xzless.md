---
layout: page
title: common/xzless (English)
description: "Display text from `xz` and `lzma` compressed files."
content_hash: b612dee26e23615164764d5c02ee0b543deb88a4
last_modified_at: 2023-07-16
---
# xzless

Display text from `xz` and `lzma` compressed files.
See also: `less`.
More information: <https://manned.org/xzless>.

- View a compressed file:

`xzless `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- View a compressed file and display line numbers:

`xzless --LINE-NUMBERS `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- View a compressed file and quit if the entire file can be displayed on the first screen:

`xzless --quit-if-one-screen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
