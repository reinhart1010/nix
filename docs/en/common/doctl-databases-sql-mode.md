---
layout: page
title: common/doctl-databases-sql-mode (English)
description: "View and configure a MySQL database cluster’s global SQL modes."
content_hash: ec6d64decd5200aa1874c0d1fcbe06e8c1afd739
last_modified_at: 2023-10-12
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># doctl databases sql-mode

View and configure a MySQL database cluster’s global SQL modes.
More information: <https://docs.digitalocean.com/reference/doctl/reference/databases/sql-mode/>.

- Run a `doctl databases sql-mode` command with an access token:

`doctl databases sql-mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">access_token</span>

- Get a MySQL database cluster's SQL modes:

`doctl databases sql-mode get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_id</span>

- Overwrite a MySQL database cluster's SQL modes to the specified modes:

`doctl databases sql-mode set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sql_mode_1 sql_mode_2 ...</span>
