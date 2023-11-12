---
layout: page
title: common/csvtool (English)
description: "Utility to filter and extract data from CSV formatted sources."
content_hash: 67000fb667b846c7e6b424ef71024fa7eeacd3c8
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# csvtool

Utility to filter and extract data from CSV formatted sources.
More information: <https://github.com/maroofi/csvtool>.

- Extract the second column from a CSV file:

`csvtool --column `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.csv</span>

- Extract the second and fourth columns from a CSV file:

`csvtool --column `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2,4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.csv</span>

- Extract lines from a CSV file where the second column exactly matches 'Foo':

`csvtool --column `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` --search '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">^Foo$</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.csv</span>

- Extract lines from a CSV file where the second column starts with 'Bar':

`csvtool --column `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` --search '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">^Bar</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.csv</span>

- Find lines in a CSV file where the second column ends with 'Baz' and then extract the third and sixth columns:

`csvtool --column `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` --search '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Baz$</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.csv</span>` | csvtool --no-header --column `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3,6</span>
