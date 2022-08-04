---
layout: page
title: common/mysqldump (English)
description: "Backups MySQL databases."
content_hash: bcfbfba484550bff4973cbafe0c9bbad33e6510d
related_topics:
  - title: español version
    url: /es/common/mysqldump.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/mysqldump.html
    icon: bi bi-globe
---
# mysqldump

Backups MySQL databases.
See also `mysql` for restoring databases.
More information: <https://dev.mysql.com/doc/refman/en/mysqldump.html>.

- Create a backup (user will be prompted for a password):

`mysqldump --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>` --result-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sql</span>

- Backup a specific table redirecting the output to a file (user will be prompted for a password):

`mysqldump --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table_name</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sql</span>

- Backup all databases redirecting the output to a file (user will be prompted for a password):

`mysqldump --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` --password --all-databases > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sql</span>

- Backup all databases from a remote host, redirecting the output to a file (user will be prompted for a password):

`mysqldump --host={(ip_or_hostname)} --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` --password --all-databases > ({path/to/file.sql</span>
