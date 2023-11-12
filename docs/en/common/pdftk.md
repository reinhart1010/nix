---
layout: page
title: common/pdftk (English)
description: "PDF toolkit."
content_hash: 6ecd03473f85965d3647257df47a9d8b60693ec3
last_modified_at: 2023-11-12
related_topics:
  - title: polski version
    url: /pl/common/pdftk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/pdftk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pdftk

PDF toolkit.
More information: <https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit>.

- Extract pages 1-3, 5 and 6-10 from a PDF file and save them as another one:

`pdftk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.pdf</span>` cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-3 5 6-10</span>` output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.pdf</span>

- Merge (concatenate) a list of PDF files and save the result as another one:

`pdftk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1.pdf file2.pdf ...</span>` cat output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.pdf</span>

- Split each page of a PDF file into a separate file, with a given filename output pattern:

`pdftk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.pdf</span>` burst output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">out_%d.pdf</span>

- Rotate all pages by 180 degrees clockwise:

`pdftk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.pdf</span>` cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-endsouth</span>` output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.pdf</span>

- Rotate third page by 90 degrees clockwise and leave others unchanged:

`pdftk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.pdf</span>` cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-2 3east 4-end</span>` output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.pdf</span>
