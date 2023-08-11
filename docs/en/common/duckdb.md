---
layout: page
title: common/duckdb (English)
description: "Command-line client for DuckDB, an in-process analytical SQL engine."
content_hash: e79ec0686e357aa1b5ae29c53f1c84b8e60eae1e
last_modified_at: 2023-08-11
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># duckdb

Command-line client for DuckDB, an in-process analytical SQL engine.
More information: <https://duckdb.org>.

- Start an interactive shell with a transient in-memory database:

`duckdb`

- Start an interactive shell on a database file. If the file does not exist, a new database is created:

`duckdb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/dbfile</span>

- Directly query a CSV, JSON, or Parquet file:

`duckdb -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SELECT * FROM 'data_source.[csv|csv.gz|json|json.gz|parquet]'</span>`"`

- Run a SQL script:

`duckdb -c ".read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sql</span>`"`

- Run query on database file and keep the interactive shell open:

`duckdb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/dbfile</span>` -cmd "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SELECT DISTINCT * FROM tbl</span>`"`

- Run SQL queries in file on database and keep the interactive shell open:

`duckdb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/dbfile</span>` -init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sql</span>

- Read CSV from stdin and write CSV to stdout:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.csv</span>` | duckdb -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">COPY (FROM read_csv_auto('/dev/stdin')) TO '/dev/stdout' WITH (FORMAT CSV, HEADER)</span>`"`

- Display help:

`duckdb -help`
