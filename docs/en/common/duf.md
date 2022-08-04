---
layout: page
title: common/duf (English)
description: "Disk Usage/Free Utility."
content_hash: 80581b41a845644853ebd9f0fede4c4c616d2b3a
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># duf

Disk Usage/Free Utility.
More information: <https://github.com/muesli/duf>.

- List accessible devices:

`duf`

- List everything (such as pseudo, duplicate or inaccessible file systems):

`duf --all`

- Only show specified devices or mount points:

`duf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory1 path/to/directory2 ...</span>

- Sort the output by a specified criteria:

`duf --sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size|used|avail|usage</span>
