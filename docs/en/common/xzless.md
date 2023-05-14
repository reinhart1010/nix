---
layout: page
title: common/xzless (English)
description: "Display text from `.xz` and `.lzma` files."
content_hash: f9dd1e2ed8bc7da2fa9e44fd7caa8e84645c369e
last_modified_at: 2023-05-14
---
# xzless

Display text from `.xz` and `.lzma` files.
See also: `less`.
More information: <https://manned.org/xzless>.

- View a compressed file:

`xzless `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive</span>

- View a compressed file and display line numbers:

`xzless --LINE-NUMBERS `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive</span>

- View a compressed file and quit if the entire file can be displayed on the first screen:

`xzless --quit-if-one-screen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive</span>
