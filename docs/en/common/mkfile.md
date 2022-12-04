---
layout: page
title: common/mkfile (English)
description: "Create one or more empty files of any size."
content_hash: 8e4b0c6b5c00fa52c9994e0375306d1bfb8b7a11
last_modified_at: 2022-12-04
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mkfile

Create one or more empty files of any size.
More information: <https://manned.org/mkfile>.

- Create an empty file of 15 kilobytes:

`mkfile -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">15k</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Create a file of a given size and unit (bytes, KB, MB, GB):

`mkfile -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">b|k|m|g</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Create two files of 4 megabytes each:

`mkfile -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4m</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">first_filename</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">second_filename</span>
