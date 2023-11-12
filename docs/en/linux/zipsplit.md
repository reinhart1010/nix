---
layout: page
title: linux/zipsplit (English)
description: "Read a zipfile and split it into smaller zipfiles."
content_hash: 6b6329931596f1441e345036ce5d3dc433e1a83b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# zipsplit

Read a zipfile and split it into smaller zipfiles.
More information: <https://manned.org/zipsplit>.

- Split zipfile into pieces that are no larger than a particular size [n]:

`zipsplit -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.zip</span>

- [p]ause between the creation of each split zipfile:

`zipsplit -p -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.zip</span>

- Output the split zipfiles into the `archive` directory:

`zipsplit -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive</span>` -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.zip</span>
