---
layout: page
title: common/mysqld (English)
description: "Start the MySQL database server."
content_hash: 326f809b46584f04f99e0dc9386c8d3befda5a04
last_modified_at: 2023-11-12
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

- Show all help options and exit:

`mysqld --verbose --help`
