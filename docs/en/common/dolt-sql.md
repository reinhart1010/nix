---
layout: page
title: common/dolt-sql (English)
description: "Run an SQL query. Multiple SQL statements must be separated by semicolons."
content_hash: 575a56201d060088f118f72f723c1f4a0e944d65
last_modified_at: 2024-02-23
tldri18n_status: 2
---
# dolt sql

Run an SQL query. Multiple SQL statements must be separated by semicolons.
More information: <https://docs.dolthub.com/cli-reference/cli#dolt-sql>.

- Run a single query:

`dolt sql --query "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">INSERT INTO t values (1, 3);</span>`"`

- List all saved queries:

`dolt sql --list-saved`
