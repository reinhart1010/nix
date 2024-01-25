---
layout: page
title: common/find (English)
description: "Find files or directories under the given directory tree, recursively."
content_hash: fcb237cf19d21dc997e3ab0a1c34f0588ea3d3f9
last_modified_at: 2024-01-25
related_topics:
  - title: français version
    url: /fr/common/find.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/find.html
    icon: bi bi-globe
tldri18n_status: 2
---
# find

Find files or directories under the given directory tree, recursively.
More information: <https://manned.org/find>.

- Find files by extension:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">root_path</span>` -name '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>`'`

- Find files matching multiple path/name patterns:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">root_path</span>` -path '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">**/path/**/*.ext</span>`' -or -name '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*pattern*</span>`'`

- Find directories matching a given name, in case-insensitive mode:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">root_path</span>` -type d -iname '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*lib*</span>`'`

- Find files matching a given pattern, excluding specific paths:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">root_path</span>` -name '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.py</span>`' -not -path '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*/site-packages/*</span>`'`

- Find files matching a given size range, limiting the recursive depth to "1":

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">root_path</span>` -maxdepth 1 -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+500k</span>` -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-10M</span>

- Run a command for each file (use `{}` within the command to access the filename):

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">root_path</span>` -name '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>`' -exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wc -l</span>` {} \;`

- Find all files modified today and pass the results to a single command as arguments:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">root_path</span>` -daystart -mtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-1</span>` -exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tar -cvf archive.tar</span>` {} \+`

- Find empty (0 byte) files and delete them:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">root_path</span>` -type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">f</span>` -empty -delete`
