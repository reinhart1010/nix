---
layout: page
title: common/cypher-shell (English)
description: "Open an interactive session and run Cypher queries against a Neo4j instance."
content_hash: e8a561208e9ddb3c7c138bda67fb11a5acbabf97
last_modified_at: 2024-06-19
tldri18n_status: 2
---
# cypher-shell

Open an interactive session and run Cypher queries against a Neo4j instance.
See also: `neo4j-admin`, `mysql`.
More information: <https://neo4j.com/docs/operations-manual/current/tools/cypher-shell/>.

- Connect to a local instance on the default port (`neo4j://localhost:7687`):

`cypher-shell`

- Connect to a remote instance:

`cypher-shell --address neo4j://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Connect and supply security credentials:

`cypher-shell --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Connect to a specific database:

`cypher-shell --database `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>

- Execute Cypher statements in a file and close:

`cypher-shell --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.cypher</span>

- Enable logging to a file:

`cypher-shell --log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.log</span>

- Display help:

`cypher-shell --help`
