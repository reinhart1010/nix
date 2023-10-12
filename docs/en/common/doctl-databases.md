---
layout: page
title: common/doctl-databases (English)
description: "Manage your MySQL, Redis, PostgreSQL, and MongoDB database services."
content_hash: f1743b1569670e89260dd1bf56ae8429c05ba71b
last_modified_at: 2023-10-12
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># doctl databases

Manage your MySQL, Redis, PostgreSQL, and MongoDB database services.
More information: <https://docs.digitalocean.com/reference/doctl/reference/databases>.

- Run a `doctl databases` command with an access token:

`doctl databases `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">access_token</span>

- Get details for a database cluster:

`doctl databases get`

- List your database clusters:

`doctl databases list`

- Create a database cluster:

`doctl databases create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>

- Delete a cluster:

`doctl databases delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_id</span>
