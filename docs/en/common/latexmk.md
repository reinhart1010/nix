---
layout: page
title: common/latexmk (English)
description: "Compile LaTeX source files into finished documents."
content_hash: 1e63cdd1d6d86cc129c8fe94628bdcf4763bc967
last_modified_at: 2024-04-10
tldri18n_status: 2
---
# latexmk

Compile LaTeX source files into finished documents.
Automatically does multiple runs when needed.
More information: <https://mg.readthedocs.io/latexmk.html>.

- Compile a DVI (Device Independent file) document from every source:

`latexmk`

- Compile a DVI document from a specific source file:

`latexmk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.tex</span>

- Compile a PDF document:

`latexmk -pdf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.tex</span>

- Open the document in a viewer and continuously update it whenever source files change:

`latexmk -pvc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.tex</span>

- Force the generation of a document even if there are errors:

`latexmk -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.tex</span>

- Clean up temporary TEX files created for a specific TEX file:

`latexmk -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.tex</span>

- Clean up all temporary TEX files in the current directory:

`latexmk -c`
