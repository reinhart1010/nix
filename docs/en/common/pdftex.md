---
layout: page
title: common/pdftex (English)
description: "Compile a PDF document from TeX source files."
content_hash: 25d82d97ecbd4f72a6ccebe08745c2815c2556d0
related_topics:
  - title: Deutsch version
    url: /de/common/pdftex.html
    icon: bi bi-globe
---
# pdftex

Compile a PDF document from TeX source files.
More information: <https://www.tug.org/applications/pdftex/>.

- Compile a PDF document:

`pdftex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.tex</span>

- Compile a PDF document, specifying an output directory:

`pdftex -output-directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.tex</span>

- Compile a PDF document, exiting on each error:

`pdftex -halt-on-error `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.tex</span>
