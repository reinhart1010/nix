---
layout: page
title: linux/lrunzip (English)
description: "A large file decompression program."
content_hash: 3626fb6b4c046cb8fca8d47c292a52133f37add6
last_modified_at: 2023-11-23
tldri18n_status: 2
---
# lrunzip

A large file decompression program.
See also: `lrzip`, `lrztar`, `lrzuntar`.
More information: <https://manned.org/lrunzip>.

- Decompress a file:

`lrunzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.lrz</span>

- Decompress a file using a specific number of processor threads:

`lrunzip -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.lrz</span>

- Decompress a file and silently overwrite files if they exist:

`lrunzip -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.lrz</span>

- Keep broken or damaged files instead of deleting them when decompressing:

`lrunzip -K `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.lrz</span>

- Specify output file name and/or path:

`lrunzip -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">outfilename</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.lrz</span>
