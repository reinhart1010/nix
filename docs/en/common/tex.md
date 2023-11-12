---
layout: page
title: common/tex (English)
description: "Compile a DVI document from TeX source files."
content_hash: 9de74854d2f7933284e729cf4c36360c273f8b0c
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/tex.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tex

Compile a DVI document from TeX source files.
More information: <https://www.tug.org/begin.html>.

- Compile a DVI document:

`tex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.tex</span>

- Compile a DVI document, specifying an output directory:

`tex -output-directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.tex</span>

- Compile a DVI document, exiting on each error:

`tex -halt-on-error `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.tex</span>
