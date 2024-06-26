---
layout: page
title: common/in2csv (English)
description: "Convert various tabular data formats to CSV."
content_hash: 04e05a22d9b4309c1892658422b3c1abb94a7765
last_modified_at: 2024-04-26
tldri18n_status: 2
---
# in2csv

Convert various tabular data formats to CSV.
Included in csvkit.
More information: <https://csvkit.readthedocs.io/en/latest/scripts/in2csv.html>.

- Convert an XLS file to CSV:

`in2csv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.xls</span>

- Convert a DBF file to a CSV file:

`in2csv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.dbf</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>

- Convert a specific sheet from an XLSX file to CSV:

`in2csv --sheet=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sheet_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.xlsx</span>

- Pipe a JSON file to in2csv:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.json</span>` | in2csv -f json > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>
