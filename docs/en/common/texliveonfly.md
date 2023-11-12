---
layout: page
title: common/texliveonfly (English)
description: "Downloads missing TeX Live packages while compiling `.tex` files."
content_hash: bec45039f3f0fc109d4804adb5fd64b6460023ba
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/texliveonfly.html
    icon: bi bi-globe
tldri18n_status: 2
---
# texliveonfly

Downloads missing TeX Live packages while compiling `.tex` files.
More information: <https://ctan.org/pkg/texliveonfly>.

- Download missing packages while compiling:

`texliveonfly `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.tex</span>

- Use a specific compiler (defaults to `pdflatex`):

`texliveonfly --compiler=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">compiler</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.tex</span>

- Use a custom TeX Live `bin` folder:

`texliveonfly --texlive_bin=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/texlive_bin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.tex</span>
