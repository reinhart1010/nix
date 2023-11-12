---
layout: page
title: common/doctl-databases-replica (English)
description: "Manage read-only replicas associated with a database cluster."
content_hash: 7375d6a9da2679f076423de320ef2075ac40c49f
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# doctl databases replica

Manage read-only replicas associated with a database cluster.
More information: <https://docs.digitalocean.com/reference/doctl/reference/databases/replica/>.

- Run a `doctl databases replica` command with an access token:

`doctl databases pool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">access_token</span>

- Retrieve information about a read-only database replica:

`doctl databases replica get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">replica_name</span>

- Retrieve list of read-only database replicas:

`doctl databases replica list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_id</span>

- Create a read-only database replica:

`doctl databases replica create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">replica_name</span>

- Delete a read-only database replica:

`doctl databases replica delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">replica_name</span>
