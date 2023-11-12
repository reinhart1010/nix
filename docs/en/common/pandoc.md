---
layout: page
title: common/pandoc (English)
description: "Convert documents between various formats."
content_hash: b6e12474bf6c316bd637a5d5721c70c5f2710a38
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pandoc

Convert documents between various formats.
More information: <https://pandoc.org>.

- Convert file to PDF (the output format is determined by file extension):

`pandoc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.md</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.pdf</span>

- Force conversion to use a specific format:

`pandoc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.docx</span>` --to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gfm</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.md</span>

- Convert to a standalone file with the appropriate headers/footers (for LaTeX, HTML, etc.):

`pandoc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.md</span>` -s -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.tex</span>

- List all supported input formats:

`pandoc --list-input-formats`

- List all supported output formats:

`pandoc --list-output-formats`
