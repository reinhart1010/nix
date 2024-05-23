---
layout: page
title: common/xdelta (English)
description: "Delta encoding utility."
content_hash: 03af6b2fb57355923ee67e811bdf6ddb9d840788
last_modified_at: 2024-05-23
tldri18n_status: 2
---
# xdelta

Delta encoding utility.
Often used for applying patches to binary files.
More information: <https://github.com/jmacd/xdelta>.

- Apply a patch:

`xdelta -d -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/delta_file.xdelta</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Create a patch:

`xdelta -e -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/old_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/new_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.xdelta</span>
