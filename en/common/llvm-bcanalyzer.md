---
layout: page
title: common/llvm-bcanalyzer (English)
description: "LLVM Bitcode (`.bc`) analyzer."
content_hash: cff093f93bf248938fa39617acd255a07bda1e37
---
# llvm-bcanalyzer

LLVM Bitcode (`.bc`) analyzer.
More information: <https://llvm.org/docs/CommandGuide/llvm-bcanalyzer.html>.

- Print statistics about a Bitcode file:

`llvm-bcanalyzer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bc</span>

- Print an SGML representation and statistics about a Bitcode file:

`llvm-bcanalyzer -dump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bc</span>

- Read a Bitcode file from `stdin` and analyze it:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bc</span>` | llvm-bcanalyzer`
