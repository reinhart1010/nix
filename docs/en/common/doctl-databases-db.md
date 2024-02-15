---
layout: page
title: common/doctl-databases-db (English)
description: "Manage databases that are served by a database cluster."
content_hash: 5396c7f19b942b745b7833d4139600e8de2b2abb
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# doctl databases db

Manage databases that are served by a database cluster.
More information: <https://docs.digitalocean.com/reference/doctl/reference/databases/db>.

- Run a `doctl databases db` command with an access token:

`doctl databases db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">access_token</span>

- Retrieve the name of the given database hosted in the given database cluster:

`doctl databases db get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>

- List existing databases hosted within a given database cluster:

`doctl databases db list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_id</span>

- Create a database with the given name in the given database cluster:

`doctl databases db create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>

- Delete the database with the given name in the given database cluster:

`doctl databases db delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>
