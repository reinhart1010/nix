---
layout: page
title: common/q (English)
description: "Execute SQL-like queries on .csv and .tsv files."
content_hash: d75bf1807e9b0c29b4eb0feb75ed7dcdd43cc8e3
last_modified_at: 2024-02-05
tldri18n_status: 2
---
# q

Execute SQL-like queries on .csv and .tsv files.
More information: <https://harelba.github.io/q>.

- Query `.csv` file by specifying the delimiter as ',':

`q -d',' "SELECT * from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`"`

- Query `.tsv` file:

`q -t "SELECT * from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`"`

- Query file with header row:

`q -d`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">delimiter</span>` -H "SELECT * from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`"`

- Read data from `stdin`; '-' in the query represents the data from `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output</span>` | q "select * from -"`

- Join two files (aliased as `f1` and `f2` in the example) on column `c1`, a common column:

`q "SELECT * FROM `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` f1 JOIN `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/other_file</span>` f2 ON (f1.c1 = f2.c1)"`

- Format output using an output delimiter with an output header line (Note: command will output column names based on the input file header or the column aliases overridden in the query):

`q -D`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">delimiter</span>` -O "SELECT `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">column</span>` as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias</span>` from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`"`
