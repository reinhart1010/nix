---
layout: page
title: common/egrep (English)
description: "Find patterns in files using extended regular expression (supports `?`, `+`, `{}`, `()` and `|`)."
content_hash: fbfa13406dfe7980ab7846f89152b499ec7e6c01
last_modified_at: 2024-01-31
related_topics:
  - title: français version
    url: /fr/common/egrep.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/egrep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# egrep

Find patterns in files using extended regular expression (supports `?`, `+`, `{}`, `()` and `|`).
More information: <https://manned.org/egrep>.

- Search for a pattern within a file:

`egrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Search for a pattern within multiple files:

`egrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Search `stdin` for a pattern:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | egrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>

- Print file name and line number for each match:

`egrep --with-filename --line-number "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Search for a pattern in all files recursively in a directory, ignoring binary files:

`egrep --recursive --binary-files=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">without-match</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Search for lines that do not match a pattern:

`egrep --invert-match "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
