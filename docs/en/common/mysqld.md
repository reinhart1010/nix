---
layout: page
title: common/mysqld (English)
description: "Start the MySQL database server."
content_hash: 3d2993157234eb0d4a500c80627e67cdc43d5e49
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# mysqld

Start the MySQL database server.
More information: <https://dev.mysql.com/doc/refman/en/mysqld.html>.

- Start the MySQL database server:

`mysqld`

- Start the server, printing error messages to the console:

`mysqld --console`

- Start the server, saving logging output to a custom log file:

`mysqld --log=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.log</span>

- Print the default arguments and their values and exit:

`mysqld --print-defaults`

- Start the server, reading arguments and values from a file:

`mysqld --defaults-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Start the server and listen on a custom port:

`mysqld --port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Display help:

`mysqld --verbose --help`
