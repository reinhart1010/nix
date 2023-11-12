---
layout: page
title: common/cbt (English)
description: "Utility for reading data from Google Cloud's Bigtable."
content_hash: 7808ab7a80f52acec38febe45f97e782ca24edee
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# cbt

Utility for reading data from Google Cloud's Bigtable.
More information: <https://cloud.google.com/bigtable/docs/cbt-reference>.

- List tables in the current project:

`cbt ls`

- Print count of rows in a specific table in the current project:

`cbt count "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table_name</span>`"`

- Display a single row from a specific table with only 1 (most recent) cell revision per column in the current project:

`cbt lookup "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table_name</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">row_key</span>`" cells-per-column=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Display a single row with only specific column(s) (omit qualifier to return entire family) in the current project:

`cbt lookup "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table_name</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">row_key</span>`" columns="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">family1:qualifier1,family2:qualifier2,...</span>`"`

- Search up to 5 rows in the current project by a specific regex pattern and print them:

`cbt read "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table_name</span>`" regex="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">row_key_pattern</span>`" count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- Read a specific range of rows and print only returned row keys in the current project:

`cbt read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table_name</span>` start=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start_row_key</span>` end=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">end_row_key</span>` keys-only=true`
