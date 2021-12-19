---
layout: page
title: common/tac (English)
description: "Print and concatenate files in reverse (last line first)."
content_hash: 209da0bc9131ea62eaacbc8172cf4bf3e8ae938d
related_topics:
  - title: italiano version
    url: /it/common/tac.html
    icon: bi bi-globe
---
# tac

Print and concatenate files in reverse (last line first).
More information: <https://www.gnu.org/software/coreutils/tac>.

- Print the contents of *file1* reversed to the standard output:

`tac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>

- Print the contents of the standard input reversed to the standard output:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | tac`

- Concatenate several files reversed into the target file:

`tac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_file</span>
