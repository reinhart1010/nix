---
layout: page
title: common/dolt-sql (English)
description: "Run a SQL query. Multiple SQL statements must be separated by semicolons."
content_hash: 8c012b32b886f553567b519b4d4b6868e0bea020
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dolt sql

Run a SQL query. Multiple SQL statements must be separated by semicolons.
More information: <https://docs.dolthub.com/cli-reference/cli#dolt-sql>.

- Run a single query:

`dolt sql --query "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">INSERT INTO t values (1, 3);</span>`"`

- List all saved queries:

`dolt sql --list-saved`
