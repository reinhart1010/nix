---
layout: page
title: common/sqlite3 (English)
description: "The command-line interface to SQLite 3, which is a self-contained file-based embedded SQL engine."
content_hash: 3986229705715802281c27faace38b9ef3e919dc
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/sqlite3.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sqlite3

The command-line interface to SQLite 3, which is a self-contained file-based embedded SQL engine.
More information: <https://sqlite.org>.

- Start an interactive shell with a new database:

`sqlite3`

- Open an interactive shell against an existing database:

`sqlite3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database.sqlite3</span>

- Execute an SQL statement against a database and then exit:

`sqlite3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database.sqlite3</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SELECT * FROM some_table;</span>`'`
