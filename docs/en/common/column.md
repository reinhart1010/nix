---
layout: page
title: common/column (English)
description: "Format standard input or a file into multiple columns."
content_hash: d85c018ce84a7ec85b36dc730abc7183b38d3a21
related_topics:
  - title: italiano version
    url: /it/common/column.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/column.html
    icon: bi bi-globe
---
# column

Format standard input or a file into multiple columns.
Columns are filled before rows; the default separator is a whitespace.
More information: <https://manned.org/column>.

- Format the output of a command for a 30 characters wide display:

`printf "header1 header2\nbar foo\n" | column --output-width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>

- Split columns automatically and auto-align them in a tabular format:

`printf "header1 header2\nbar foo\n" | column --table`

- Specify the column delimiter character for the `--table` option (e.g. "," for CSV) (defaults to whitespace):

`printf "header1,header2\nbar,foo\n" | column --table --separator `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>

- Fill rows before filling columns:

`printf "header1\nbar\nfoobar\n" | column --output-width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>` --fillrows`
