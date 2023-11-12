---
layout: page
title: common/mlr (English)
description: "Miller is like `awk`, `sed`, `cut`, `join`, and `sort` for name-indexed data such as CSV, TSV, and tabular JSON."
content_hash: f9f1cbe64c3fa5676efd0585c2bd17bb6f2b92d9
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# mlr

Miller is like `awk`, `sed`, `cut`, `join`, and `sort` for name-indexed data such as CSV, TSV, and tabular JSON.
More information: <https://johnkerl.org/miller/doc>.

- Pretty-print a CSV file in a tabular format:

`mlr --icsv --opprint cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.csv</span>

- Receive JSON data and pretty print the output:

`echo '{"hello":"world"}' | mlr --ijson --opprint cat`

- Sort alphabetically on a field:

`mlr --icsv --opprint sort -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">field</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.csv</span>

- Sort in descending numerical order on a field:

`mlr --icsv --opprint sort -nr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">field</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.csv</span>

- Convert CSV to JSON, performing calculations and display those calculations:

`mlr --icsv --ojson put '$`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">newField1</span>` = $`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">oldFieldA</span>`/$`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">oldFieldB</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.csv</span>

- Receive JSON and format the output as vertical JSON:

`echo '{"hello":"world", "foo":"bar"}' | mlr --ijson --ojson --jvstack cat`

- Filter lines of a compressed CSV file treating numbers as strings:

`mlr --prepipe 'gunzip' --csv filter -S '$`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fieldName</span>` =~ "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`"' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.csv.gz</span>
