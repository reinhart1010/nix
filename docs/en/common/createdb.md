---
layout: page
title: common/createdb (English)
description: "Create a PostgreSQL database."
content_hash: 6acde9efaf358d2cad2aa076e5e07cd4e4d190fc
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# createdb

Create a PostgreSQL database.
More information: <https://www.postgresql.org/docs/current/app-createdb.html>.

- Create a database owned by the current user:

`createdb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>

- Create a database owned by a specific user with a description:

`createdb --owner=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">description</span>`'`

- Create a database from a template:

`createdb --template=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">template_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>
