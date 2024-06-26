---
layout: page
title: common/neo4j-admin (English)
description: "Manage and administer a Neo4j DBMS (Database Management System)."
content_hash: 8f7932fc4d520f45e08920a98e23ced217bba94e
last_modified_at: 2024-06-18
tldri18n_status: 2
---
# neo4j-admin

Manage and administer a Neo4j DBMS (Database Management System).
See also: `cypher-shell`, `mysqld`.
More information: <https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/>.

- Start the DBMS:

`neo4j-admin server start`

- Stop the DBMS:

`neo4j-admin server stop`

- Set the initial password of the default `neo4j` user (prerequisite for the first start of the DBMS):

`neo4j-admin dbms set-initial-password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>

- Create an archive (dump) of an offline database to a file named `database_name.dump`:

`neo4j-admin database dump --to-path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>

- Load a database from an archive named `database_name.dump`:

`neo4j-admin database load --from-path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>` --overwrite-destination=true`

- Load a database from a specified archive file through `stdin`:

`neo4j-admin database load --from-stdin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>` --overwrite-destination=true < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filename.dump</span>

- Display help:

`neo4j-admin --help`
