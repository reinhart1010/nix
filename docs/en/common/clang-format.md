---
layout: page
title: common/clang-format (English)
description: "Auto-format C/C++/Java/JavaScript/Objective-C/Protobuf/C# code."
content_hash: 34f9ce6cff4d5640423e7f62f002d2177cb1f5bd
last_modified_at: 2024-04-19
related_topics:
  - title: Deutsch version
    url: /de/common/clang-format.html
    icon: bi bi-globe
tldri18n_status: 2
---
# clang-format

Auto-format C/C++/Java/JavaScript/Objective-C/Protobuf/C# code.
More information: <https://clang.llvm.org/docs/ClangFormat.html>.

- Format a file and print the result to `stdout`:

`clang-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Format a file in-place:

`clang-format -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Format a file using a predefined coding style:

`clang-format --style `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">LLVM|GNU|Google|Chromium|Microsoft|Mozilla|WebKit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Format a file using the `.clang-format` file in one of the parent directories of the source file:

`clang-format --style=file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Generate a custom `.clang-format` file:

`clang-format --style `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">LLVM|GNU|Google|Chromium|Microsoft|Mozilla|WebKit</span>` --dump-config > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.clang-format</span>
