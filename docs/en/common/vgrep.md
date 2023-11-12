---
layout: page
title: common/vgrep (English)
description: "A user friendly pager for grep."
content_hash: a9257117d4c4efe7d2c6795039e3c91bbb41cdfd
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# vgrep

A user friendly pager for grep.
See also: `ugrep`, `rg`.
More information: <https://github.com/vrothberg/vgrep>.

- Recursively search the current directory for a pattern and cache it:

`vgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>

- Display the contents of the cache:

`vgrep`

- Open the "4th" match from the cache in the default editor:

`vgrep --show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- Display a context of "3" lines for each match in the cache:

`vgrep --show=context`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- Display the number of matches for each directory in the tree:

`vgrep --show=tree`

- Display the number of matches for each file in the tree:

`vgrep --show=files`

- Start an interactive shell with cached matches:

`vgrep --interactive`
