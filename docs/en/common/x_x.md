---
layout: page
title: common/x_x (English)
description: "View Excel and CSV files from the command-line."
content_hash: e21dc06c0861e946468785c6547f1cb587b3543b
---
# x_x

View Excel and CSV files from the command-line.
More information: <https://github.com/kristianperkins/x_x>.

- View an XLSX or CSV file:

`x_x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.xlsx|file.csv</span>

- View an XLSX or CSV file, using the first row as table headers:

`x_x -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.xlsx|file.csv</span>

- View a CSV file with unconventional delimiters:

`x_x --delimiter=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">';'</span>` --quotechar=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'|'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.csv</span>
