---
layout: page
title: common/git-filter-repo (English)
description: "A versatile tool for rewriting Git history."
content_hash: 38bef94e6ff449f1e33837fb4a0dea330f07137c
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git filter-repo

A versatile tool for rewriting Git history.
See also: `bfg`.
More information: <https://github.com/newren/git-filter-repo>.

- Replace a sensitive string in all files:

`git filter-repo --replace-text <(echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find</span>`==>`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">replacement</span>`')`

- Extract a single folder, keeping history:

`git-filter-repo --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/folder</span>

- Remove a single folder, keeping history:

`git-filter-repo --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/folder</span>` --invert-paths`

- Move everything from sub-folder one level up:

`git-filter-repo --path-rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/folder/:</span>
