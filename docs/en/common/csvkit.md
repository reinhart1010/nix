---
layout: page
title: common/csvkit (English)
description: "Manipulation toolkit for CSV files."
content_hash: ddd7383344d25e907de9647f4c9f8d8732a3d7a2
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# csvkit

Manipulation toolkit for CSV files.
See also: `csvclean`, `csvcut`, `csvformat`, `csvgrep`, `csvlook`, `csvpy`, `csvsort`, `csvstat`.
More information: <https://csvkit.readthedocs.io/en/0.9.1/cli.html>.

- Run a command on a CSV file with a custom delimiter:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">delimiter</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.csv</span>

- Run a command on a CSV file with a tab as a delimiter (overrides -d):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.csv</span>

- Run a command on a CSV file with a custom quote character:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quote_char</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.csv</span>

- Run a command on a CSV file with no header row:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` -H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.csv</span>
