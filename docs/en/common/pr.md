---
layout: page
title: common/pr (English)
description: "Paginate or columnate files for printing."
content_hash: c232a31fd815911969147f9abb45ffe25f13a5c7
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/common/pr.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pr

Paginate or columnate files for printing.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/pr-invocation.html>.

- Print multiple files with a default header and footer:

`pr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Print with a custom centered header:

`pr -h "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">header</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Print with numbered lines and a custom date format:

`pr -n -D "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">format</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Print all files together, one in each column, without a header or footer:

`pr -m -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Print, beginning at page 2 up to page 5, with a given page length (including header and footer):

`pr +2:5 -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">page_length</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Print with an offset for each line and a truncating custom page width:

`pr -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">offset</span>` -W `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>
