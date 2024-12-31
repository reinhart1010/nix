---
layout: page
title: common/latexpand (English)
description: "Simplify LaTeX source files by removing comments and resolving `\include`s, `\input`s, etc."
content_hash: 2a710c083fe3a0e7aad7a5e9fa107f9b65f7ef25
last_modified_at: 2024-12-31
related_topics:
  - title: español version
    url: /es/common/latexpand.html
    icon: bi bi-globe
tldri18n_status: 2
---
# latexpand

Simplify LaTeX source files by removing comments and resolving `\include`s, `\input`s, etc.
More information: <https://www.ctan.org/pkg/latexpand>.

- Simplify the specified source file and save the result to the specified [o]utput file:

`latexpand --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.tex</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tex</span>

- Do not remove comments:

`latexpand --keep-comments --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.tex</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tex</span>

- Do not expand `\include`s, `\input`s etc.:

`latexpand --keep-includes --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.tex</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tex</span>

- Expand `\usepackage`s as far as the corresponding STY files can be found:

`latexpand --expand-usepackage --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.tex</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tex</span>

- Inline the specified BBL file:

`latexpand --expand-bbl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/bibliography.bbl</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.tex</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tex</span>
