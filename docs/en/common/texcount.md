---
layout: page
title: common/texcount (English)
description: "Count words in TeX documents omitting macros."
content_hash: 001a8359cbebdd94975ebcc82ee853cb417f7280
last_modified_at: 2024-05-12
tldri18n_status: 2
---
# texcount

Count words in TeX documents omitting macros.
Note: if the TeX document uses `\include` or `\input` and you want to count the included files, `texcount` must be run in the directory of the root TeX file.
More information: <https://app.uio.no/ifi/texcount/howto.html>.

- Count words in a TeX file:

`texcount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tex</span>

- Count words in a document and subdocuments built with `\input` or `\include`:

`texcount -merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.tex</span>

- Count words in a document and subdocuments, listing each file separately (and a total count):

`texcount -inc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.tex</span>

- Count words in a document and subdocuments, producing subcounts by chapter (instead of subsection):

`texcount -merge -sub=chapter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.tex</span>

- Count words with verbose output:

`texcount -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tex</span>
