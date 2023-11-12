---
layout: page
title: common/mysqlbinlog (English)
description: "Utility for processing MySQL binary log files."
content_hash: 2d1389c8f7595bdea973386d3e2883bbd2b555c5
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# mysqlbinlog

Utility for processing MySQL binary log files.
More information: <https://dev.mysql.com/doc/refman/8.0/en/mysqlbinlog.html>.

- Show events from a specific binary log file:

`mysqlbinlog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binlog</span>

- Show entries from a binary log for a specific database:

`mysqlbinlog --database `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binlog</span>

- Show events from a binary log between specific dates:

`mysqlbinlog --start-datetime='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2022-01-01 01:00:00</span>`' --stop-datetime='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2022-02-01 01:00:00</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binlog</span>

- Show events from a binary log between specific positions:

`mysqlbinlog --start-position=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --stop-position=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">200</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binlog</span>

- Show binary log from a MySQL server on the given host:

`mysqlbinlog --host=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binlog</span>
