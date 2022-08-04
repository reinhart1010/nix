---
layout: page
title: common/lli (English)
description: "Directly execute programs from LLVM bitcode."
content_hash: 9294787f93c0417baacead9dc925b7162856a5fc
---
# lli

Directly execute programs from LLVM bitcode.
More information: <https://www.llvm.org/docs/CommandGuide/lli.html>.

- Execute a bitcode or IR file:

`lli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ll</span>

- Execute with command line arguments:

`lli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ll</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1 argument2 ...</span>

- Enable all optimizations:

`lli -O3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ll</span>

- Load a dynamic library before linking:

`lli --dlopen=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/library.dll</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ll</span>
