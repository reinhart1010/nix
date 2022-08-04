---
layout: page
title: common/licensor (English)
description: "Write licenses to stdout."
content_hash: 9b63cd64222261bf4eac733119e37cf89a9d3302
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># licensor

Write licenses to stdout.
More information: <https://github.com/raftario/licensor>.

- Write the MIT license to a file named `LICENSE`:

`licensor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MIT</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">LICENSE</span>

- Write the MIT license with a [p]laceholder copyright notice to a file named `LICENSE`:

`licensor -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MIT</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">LICENSE</span>

- Specify a copyright holder named Bobby Tables:

`licensor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MIT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">"Bobby Tables"</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">LICENSE</span>

- Specify licence exceptions with a WITH expression:

`licensor "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Apache-2.0 WITH LLVM-exception</span>`" > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">LICENSE</span>

- List all available licenses:

`licensor --licenses`

- List all available exceptions:

`licensor --exceptions`
