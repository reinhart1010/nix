---
layout: page
title: common/tac (English)
description: "Display and concatenate files with lines in reversed order."
content_hash: 039c52634f81c084524ab2dfc19be1fba58e3068
related_topics:
  - title: italiano version
    url: /it/common/tac.html
    icon: bi bi-globe
---
# tac

Display and concatenate files with lines in reversed order.
See also: `cat`.
More information: <https://www.gnu.org/software/coreutils/tac>.

- Concatenate specific files in reversed order:

`tac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Display `stdin` in reversed order:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat path/to/file</span>` | tac`

- Use a specific [s]eparator:

`tac -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">separator</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Use a specific [r]egex as a [s]eparator:

`tac -r -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">separator</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Use a separator [b]efore each file:

`tac -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>
