---
layout: page
title: common/doctl-databases-pool (English)
description: "Manage connection pools for your database cluster."
content_hash: 172aff7bec32efe693e04c309f7bb89792be57e5
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# doctl databases pool

Manage connection pools for your database cluster.
More information: <https://docs.digitalocean.com/reference/doctl/reference/databases/pool/>.

- Run a `doctl databases pool` command with an access token:

`doctl databases pool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">access_token</span>

- Retrieve information about a database connection pool:

`doctl databases pool get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pool_name</span>

- List connection pools for a database cluster:

`doctl databases pool list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_id</span>

- Create a connection pool for a database:

`doctl databases pool create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pool_name</span>` --db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_pool_name</span>` --size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pool_size</span>

- Delete a connection pool for a database:

`doctl databases pool create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pool_name</span>
