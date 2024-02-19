---
layout: page
title: common/usql (English)
description: "Universal CLI interface for SQL databases."
content_hash: b05a8849fc553913121d57837bb47bf7da781db9
last_modified_at: 2024-02-19
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/usql.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># usql

Universal CLI interface for SQL databases.
More information: <https://github.com/xo/usql>.

- Connect to a specific database:

`usql `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sqlserver|mysql|postgres|sqlite3|...</span>`://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>

- Execute commands from a file:

`usql --file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/query.sql</span>

- Execute a specific SQL command:

`usql --command="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sql_command</span>`"`

- List databases available on the server:

`usql --list-databases`

- Run an SQL command in the `usql` prompt:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prompt</span>`=> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Display the database schema:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prompt</span>`=> \d`

- Export query results to a specific file:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prompt</span>`=> \g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/results.txt</span>

- Import data from a CSV file into a specific table:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prompt</span>`=> \copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/data.csv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table_name</span>
