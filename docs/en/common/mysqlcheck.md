---
layout: page
title: common/mysqlcheck (English)
description: "Check and repair MySQL tables."
content_hash: dd7b07f52e0568fc7f836e8fd90cde605335acd8
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# mysqlcheck

Check and repair MySQL tables.
More information: <https://dev.mysql.com/doc/refman/8.0/en/mysqlcheck.html>.

- Check a table:

`mysqlcheck --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table</span>

- Check a table and provide credentials to access it:

`mysqlcheck --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Repair a table:

`mysqlcheck --repair `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table</span>

- Optimize a table:

`mysqlcheck --optimize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table</span>
