---
layout: page
title: linux/fallocate (English)
description: "Reserve or deallocate disk space to files."
content_hash: cd664dd0d623b04fd8c794831bb8392c65a55a4f
---
# fallocate

Reserve or deallocate disk space to files.
The utility allocates space without zeroing.
More information: <https://manned.org/fallocate>.

- Reserve a file taking up 700 MiB of disk space:

`fallocate --length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">700M</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Shrink an already allocated file by 200 MiB:

`fallocate --collapse-range --length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">200M</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Shrink 20 MB of space after 100 MiB in a file:

`fallocate --collapse-range --offset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100M</span>` --length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20M</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
