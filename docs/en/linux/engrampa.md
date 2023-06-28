---
layout: page
title: linux/engrampa (English)
description: "Package files into zip/tar file in MATE desktop environment."
content_hash: 0db7408e467b39f6950bb8a908292f529bf5de19
last_modified_at: 2023-06-28
---
# engrampa

Package files into zip/tar file in MATE desktop environment.
See also: `zip`, `tar`.
More information: <https://github.com/mate-desktop/engrampa>.

- Start Engrampa:

`engrampa`

- Open specific archives:

`engrampa `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive1.tar path/to/archive2.tar ...</span>

- Archive specific files and/or directories recursively:

`engrampa --add-to=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>

- Extract files and/or directories from archives to a specific path:

`engrampa --extract-to=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive1.tar path/to/archive2.tar ...</span>
