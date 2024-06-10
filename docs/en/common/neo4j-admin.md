---
layout: page
title: common/neo4j-admin (English)
description: "Manage and administer a Neo4j DBMS (Database Management System)."
content_hash: d93a179bea24a744b27960978b2296af9e86366f
last_modified_at: 2024-06-10
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/neo4j-admin.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># neo4j-admin

Manage and administer a Neo4j DBMS (Database Management System).
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
