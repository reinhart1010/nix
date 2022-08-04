---
layout: page
title: common/pg_dumpall (English)
description: "Extract a PostgreSQL database cluster into a script file or other archive file."
content_hash: 756b774bbd970de859e6dc41049a0d5a29aa9a92
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pg_dumpall

Extract a PostgreSQL database cluster into a script file or other archive file.
More information: <https://www.postgresql.org/docs/current/app-pg-dumpall.html>.

- Dump all databases:

`pg_dumpall > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sql</span>

- Dump all databases using a specific username:

`pg_dumpall --username=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sql</span>

- Same as above, customize host and port:

`pg_dumpall -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file.sql</span>

- Dump all databases into a custom-format archive file with moderate compression:

`pg_dumpall -Fc > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file.dump</span>

- Dump only database data into an SQL-script file:

`pg_dumpall --data-only > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sql</span>

- Dump only schema (data definitions) into an SQL-script file:

`pg_dumpall -s > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file.sql</span>
