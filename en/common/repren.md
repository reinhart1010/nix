---
layout: page
title: common/repren (English)
description: "Multi-pattern string replacement and file renaming tool."
content_hash: defcdb2967c46cdd9ba0ea5b36d6eb1663e3006e
---
# repren

Multi-pattern string replacement and file renaming tool.
More information: <https://github.com/jlevy/repren>.

- Do a dry-run renaming a directory of PNGs with a literal string replacement:

`repren --dry-run --rename --literal --from '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find_string</span>`' --to '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">replacement_string</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.png</span>

- Do a dry-run renaming a directory of JPEGs with a regular expression:

`repren --rename --dry-run --from '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`' --to '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">replacement_string</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpeg</span>

- Do a find-and-replace on the contents of a directory of CSV files:

`repren --from '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">([0-9]+) example_string</span>`' --to '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">replacement_string \1</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.csv</span>

- Do both a find-and-replace and a rename operation at the same time, using a pattern file:

`repren --patterns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/patfile.ext</span>` --full `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>

- Do a case-insensitive rename:

`repren --rename --insensitive --patterns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/patfile.ext</span>` *`
