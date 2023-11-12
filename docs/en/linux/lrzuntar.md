---
layout: page
title: linux/lrzuntar (English)
description: "A wrapper for `lrunzip` to simplify decompression of directories."
content_hash: a8a28ff83d87ad08ef00c8bf83b6a0294d208660
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# lrzuntar

A wrapper for `lrunzip` to simplify decompression of directories.
See also: `lrztar`, `lrzip`.
More information: <https://manned.org/lrzuntar>.

- Decompress from a file to the current directory:

`lrzuntar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.tar.lrz</span>

- Decompress from a file to the current directory using a specific number of processor threads:

`lrzuntar -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.tar.lrz</span>

- Decompress from a file to the current directory and silently overwrite items that already exist:

`lrzuntar -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive.tar.lrz</span>

- Specify the output path:

`lrzuntar -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive.tar.lrz</span>

- Delete the compressed file after decompression:

`lrzuntar -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.tar.lrz</span>
