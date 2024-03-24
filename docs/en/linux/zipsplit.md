---
layout: page
title: linux/zipsplit (English)
description: "Split a Zip archive into smaller Zip archives."
content_hash: ae70363bd1e5e9a1748ec153da02c0ba8b0be2ee
last_modified_at: 2024-03-24
tldri18n_status: 2
---
# zipsplit

Split a Zip archive into smaller Zip archives.
More information: <https://manned.org/zipsplit>.

- Split Zip archive into parts that are no larger than 36000 bytes (36 MB):

`zipsplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.zip</span>

- Use a given [n]umber of bytes as the part limit:

`zipsplit -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.zip</span>

- [p]ause between the creation of each part:

`zipsplit -p -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.zip</span>

- Output the smaller Zip archives into a given directory:

`zipsplit -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_directory</span>` -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.zip</span>
