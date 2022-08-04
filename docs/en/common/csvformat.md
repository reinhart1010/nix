---
layout: page
title: common/csvformat (English)
description: "Convert a CSV file to a custom output format."
content_hash: 709dfdbd8ca5ee689e654f0e5c46d25f7b7f29de
related_topics:
  - title: italiano version
    url: /it/common/csvformat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/csvformat.html
    icon: bi bi-globe
---
# csvformat

Convert a CSV file to a custom output format.
Included in csvkit.
More information: <https://csvkit.readthedocs.io/en/latest/scripts/csvformat.html>.

- Convert to a tab-delimited file (TSV):

`csvformat -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>

- Convert delimiters to a custom character:

`csvformat -D "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">custom_character</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>

- Convert line endings to carriage return (^M) + line feed:

`csvformat -M "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\r\n</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>

- Minimize use of quote characters:

`csvformat -U 0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>

- Maximize use of quote characters:

`csvformat -U 1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>
