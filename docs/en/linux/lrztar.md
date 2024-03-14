---
layout: page
title: linux/lrztar (English)
description: "A wrapper for `lrzip` to simplify compression of directories."
content_hash: d268af8f0762cf2bcf4be57bd769587c8794d637
last_modified_at: 2024-03-14
tldri18n_status: 2
---
# lrztar

A wrapper for `lrzip` to simplify compression of directories.
See also: `tar`, `lrzuntar`, `lrunzip`.
More information: <https://manned.org/lrztar>.

- Archive a directory with tar, then compress:

`lrztar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Same as above, with ZPAQ - extreme compression, but very slow:

`lrztar -z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Specify the output file:

`lrztar -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Override the number of processor threads to use:

`lrztar -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Force overwriting of existing files:

`lrztar -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
