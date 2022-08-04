---
layout: page
title: common/pdflatex (English)
description: "Compile a PDF document from LaTeX source files."
content_hash: 9d8282b4d6b3c13ae34938ff68eb627715e5572a
related_topics:
  - title: Deutsch version
    url: /de/common/pdflatex.html
    icon: bi bi-globe
---
# pdflatex

Compile a PDF document from LaTeX source files.
More information: <https://manned.org/pdflatex>.

- Compile a PDF document:

`pdflatex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.tex</span>

- Compile a PDF document specifying an output directory:

`pdflatex -output-directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.tex</span>

- Compile a PDF document, exiting on each error:

`pdflatex -halt-on-error `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.tex</span>
