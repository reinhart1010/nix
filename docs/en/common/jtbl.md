---
layout: page
title: common/jtbl (English)
description: "Utility to print JSON and JSON Lines data as a table in the terminal."
content_hash: e1c384063ca4a67c701f17e10a3944e859dc5c7f
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# jtbl

Utility to print JSON and JSON Lines data as a table in the terminal.
More information: <https://github.com/kellyjonbrazil/jtbl>.

- Print a table from JSON or JSON Lines input:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.json</span>` | jtbl`

- Print a table and specify the column width for wrapping:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.json</span>` | jtbl --cols=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>

- Print a table and truncate rows instead of wrapping:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.json</span>` | jtbl -t`

- Print a table and don't wrap or truncate rows:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.json</span>` | jtbl -n`
