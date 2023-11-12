---
layout: page
title: linux/tac (English)
description: "Display and concatenate files with lines in reversed order."
content_hash: c460eed15d5039af22344f9d85ccd78c686693e2
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# tac

Display and concatenate files with lines in reversed order.
See also: `cat`.
More information: <https://www.gnu.org/software/coreutils/tac>.

- Concatenate specific files in reversed order:

`tac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Display `stdin` in reversed order:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat path/to/file</span>` | tac`

- Use a specific separator:

`tac --separator `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Use a specific regex as a separator:

`tac --regex --separator `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[,;]</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Use a separator before each file:

`tac --before `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>
