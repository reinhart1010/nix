---
layout: page
title: common/latex (English)
description: "Compile a DVI document from LaTeX source files."
content_hash: 07f099501efeba5395300698ca7b057c269ceb3e
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/latex.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/latex.html
    icon: bi bi-globe
tldri18n_status: 2
---
# latex

Compile a DVI document from LaTeX source files.
More information: <https://www.latex-project.org>.

- Compile a DVI document:

`latex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.tex</span>

- Compile a DVI document, specifying an output directory:

`latex -output-directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.tex</span>

- Compile a DVI document, exiting on each error:

`latex -halt-on-error `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.tex</span>
