---
layout: page
title: common/tabula (English)
description: "Extract tables from PDF files."
content_hash: 7996dbe3d624a42003eb80d52bee212e6aaaefb0
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# tabula

Extract tables from PDF files.
More information: <https://tabula.technology>.

- Extract all tables from a PDF to a CSV file:

`tabula -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.csv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.pdf</span>

- Extract all tables from a PDF to a JSON file:

`tabula --format JSON -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.pdf</span>

- Extract tables from pages 1, 2, 3, and 6 of a PDF:

`tabula --pages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-3,6</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.pdf</span>

- Extract tables from page 1 of a PDF, guessing which portion of the page to examine:

`tabula --guess --pages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.pdf</span>

- Extract all tables from a PDF, using ruling lines to determine cell boundaries:

`tabula --spreadsheet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.pdf</span>

- Extract all tables from a PDF, using blank space to determine cell boundaries:

`tabula --no-spreadsheet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.pdf</span>
