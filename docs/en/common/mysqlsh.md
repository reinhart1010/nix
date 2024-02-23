---
layout: page
title: common/mysqlsh (English)
description: "Advanced command-line client for MySQL, supporting SQL, JavaScript, and Python."
content_hash: b262e7885633857129fc11ab547055a6d6d76714
last_modified_at: 2024-02-23
tldri18n_status: 2
---
# mysqlsh

Advanced command-line client for MySQL, supporting SQL, JavaScript, and Python.
It offers features for managing InnoDB clusters and document store collections.
More information: <https://dev.mysql.com/doc/mysql-shell/8.0/en/mysql-shell-commands.html>.

- Start MySQL Shell in interactive mode:

`mysqlsh`

- Connect to a MySQL server:

`mysqlsh --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Execute an SQL statement on the server and exit:

`mysqlsh --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --execute '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sql_statement</span>`'`

- Start MySQL Shell in JavaScript mode:

`mysqlsh --js`

- Start MySQL Shell in Python mode:

`mysqlsh --py`

- Import JSON documents into a MySQL collection:

`mysqlsh --import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.json</span>` --schema `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">schema_name</span>` --collection `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">collection_name</span>

- Enable verbose output:

`mysqlsh --verbose`
