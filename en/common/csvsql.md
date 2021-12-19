---
layout: page
title: common/csvsql (English)
description: "Generate SQL statements for a CSV file or execute those statements directly on a database."
content_hash: b610be968ba2c99688bd43b47554cb14af66d2bc
related_topics:
  - title: Deutsch version
    url: /de/common/csvsql.html
    icon: bi bi-globe
---
# csvsql

Generate SQL statements for a CSV file or execute those statements directly on a database.
Included in csvkit.
More information: <https://csvkit.readthedocs.io/en/latest/scripts/csvsql.html>.

- Generate a `CREATE TABLE` SQL statement for a CSV file:

`csvsql `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/data.csv</span>

- Import a CSV file into an SQL database:

`csvsql --insert --db "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mysql://user:password@host/database</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>

- Run an SQL query on a CSV file:

`csvsql --query "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">select * from 'data'</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>
