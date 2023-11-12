---
layout: page
title: common/latexmk (English)
description: "Compile LaTeX source files into finished documents."
content_hash: ad9ccf5e77314c6f7c09d3977e9c4e192f7c4a66
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# latexmk

Compile LaTeX source files into finished documents.
Automatically does multiple runs when needed.
More information: <https://mg.readthedocs.io/latexmk.html>.

- Compile a DVI (Device Independent file) document from every source:

`latexmk`

- Compile a DVI document from a specific source file:

`latexmk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.tex</span>

- Compile a PDF document:

`latexmk -pdf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.tex</span>

- Force the generation of a document even if there are errors:

`latexmk -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.tex</span>

- Clean up temporary TEX files created for a specific TEX file:

`latexmk -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.tex</span>

- Clean up all temporary TEX files in the current directory:

`latexmk -c`
