---
layout: page
title: common/clang-format (English)
description: "Tool to auto-format C/C++/Java/JavaScript/Objective-C/Protobuf/C# code."
content_hash: 33fc1e9eafb8a3ddb3e34cfa73b73b5cac4a515f
last_modified_at: 2022-12-04
---
# clang-format

Tool to auto-format C/C++/Java/JavaScript/Objective-C/Protobuf/C# code.
More information: <https://clang.llvm.org/docs/ClangFormat.html>.

- Format a file and print the result to `stdout`:

`clang-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Format a file in-place:

`clang-format -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Format a file using a predefined coding style:

`clang-format --style=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">LLVM|GNU|Google|Chromium|Microsoft|Mozilla|WebKit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Format a file using the `.clang-format` file in one of the parent directories of the source file:

`clang-format --style=file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Generate a custom `.clang-format` file:

`clang-format --style=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">LLVM|GNU|Google|Chromium|Microsoft|Mozilla|WebKit</span>` --dump-config > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.clang-format</span>
