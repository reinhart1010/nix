---
layout: page
title: common/duf (English)
description: "Disk Usage/Free Utility."
content_hash: 80581b41a845644853ebd9f0fede4c4c616d2b3a
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/duf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# duf

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
