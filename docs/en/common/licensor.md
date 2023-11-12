---
layout: page
title: common/licensor (English)
description: "Write licenses to `stdout`."
content_hash: 9498bb4e385038a2a62542449a1064c922764b3b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# licensor

Write licenses to `stdout`.
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
