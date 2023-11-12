---
layout: page
title: common/lli (English)
description: "Directly execute programs from LLVM bitcode."
content_hash: def9ad6678f013e43e303eedfb2dd348b10a471f
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# lli

Directly execute programs from LLVM bitcode.
More information: <https://www.llvm.org/docs/CommandGuide/lli.html>.

- Execute a bitcode or IR file:

`lli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ll</span>

- Execute with command-line arguments:

`lli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ll</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1 argument2 ...</span>

- Enable all optimizations:

`lli -O3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ll</span>

- Load a dynamic library before linking:

`lli --dlopen=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/library.dll</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ll</span>
