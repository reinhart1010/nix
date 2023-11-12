---
layout: page
title: common/x_x (English)
description: "View Excel and CSV files."
content_hash: 3f5e5507007fad878b1186ca4504bdccd53bb134
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# x_x

View Excel and CSV files.
More information: <https://github.com/kristianperkins/x_x>.

- View an XLSX or CSV file:

`x_x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.xlsx|file.csv</span>

- View an XLSX or CSV file, using the first row as table headers:

`x_x -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.xlsx|file.csv</span>

- View a CSV file with unconventional delimiters:

`x_x --delimiter=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">';'</span>` --quotechar=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'|'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.csv</span>
