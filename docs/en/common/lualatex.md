---
layout: page
title: common/lualatex (English)
description: "An extended version of TeX using Lua to compile."
content_hash: 85e03f68a69cfa3f44b339540bf1b51e9b4711ea
---
# lualatex

An extended version of TeX using Lua to compile.
More information: <https://manned.org/lualatex.1>.

- Start `texlua` to act as a Lua interpreter:

`lualatex`

- Compile a Tex file to PDF:

`lualatex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tex</span>

- Compile a Tex file without error interruption:

`lualatex -interaction nonstopmode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tex</span>

- Compile a Tex file with a specific output file name:

`lualatex -jobname=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tex</span>
