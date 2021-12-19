---
layout: page
title: common/xetex (English)
description: "Compile a PDF document from XeTeX source files."
content_hash: d6166050f727fd10c3d20b149c865b193e8753fb
---
# xetex

Compile a PDF document from XeTeX source files.
More information: <https://www.tug.org/xetex/>.

- Compile a PDF document:

`xetex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.tex</span>

- Compile a PDF document, specifying an output directory:

`xetex -output-directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.tex</span>

- Compile a PDF document, exiting if errors occur:

`xetex -halt-on-error `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.tex</span>
