---
layout: page
title: common/llc (English)
description: "Compiles LLVM Intermediate Representation or bitcode to target-specific assembly language."
content_hash: efbc906f3ab2eed12bc5b8f6a3c733e356e4cd7a
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# llc

Compiles LLVM Intermediate Representation or bitcode to target-specific assembly language.
More information: <https://www.llvm.org/docs/CommandGuide/llc.html>.

- Compile a bitcode or IR file to an assembly file with the same base name:

`llc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ll</span>

- Enable all optimizations:

`llc -O3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.ll</span>

- Output assembly to a specific file:

`llc --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.s</span>

- Emit fully relocatable, position independent code:

`llc -relocation-model=pic `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.ll</span>
