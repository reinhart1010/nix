---
layout: page
title: common/diff-pdf (English)
description: "Tool for comparing two PDFs."
content_hash: cbb75c15fbd13d393bf31e06c8291a5cc94d79f4
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# diff-pdf

Tool for comparing two PDFs.
More information: <https://github.com/vslavik/diff-pdf>.

- Compare PDFs, indicating changes using return codes (`0` = no difference, `1` = PDFs differ):

`diff-pdf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/a.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/b.pdf</span>

- Compare PDFs, outputting a PDF with visually highlighted differences:

`diff-pdf --output-diff=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/diff.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/a.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/b.pdf</span>

- Compare PDFs, viewing differences in a simple GUI:

`diff-pdf --view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/a.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/b.pdf</span>
