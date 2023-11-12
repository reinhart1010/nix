---
layout: page
title: common/clang-tidy (English)
description: "An LLVM-based C/C++ linter to find style violations, bugs and security flaws through static analysis."
content_hash: 62b24f0cb681496b9478ac55d526af13ad0f583e
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/clang-tidy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# clang-tidy

An LLVM-based C/C++ linter to find style violations, bugs and security flaws through static analysis.
More information: <https://clang.llvm.org/extra/clang-tidy/>.

- Run default checks on a source file:

`clang-tidy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.cpp</span>

- Don't run any checks other than the `cppcoreguidelines` checks on a file:

`clang-tidy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.cpp</span>` -checks=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-*,cppcoreguidelines-*</span>

- List all available checks:

`clang-tidy -checks=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>` -list-checks`

- Specify defines and includes as compilation options (after `--`):

`clang-tidy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.cpp</span>` -- -I`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_project/include</span>` -D`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">definitions</span>
