---
layout: page
title: common/mongodump (English)
description: "Utility to export the contents of a MongoDB instance."
content_hash: 2f7f7494d1bf3c51d32f59e815a7a64f217cd561
---
# mongodump

Utility to export the contents of a MongoDB instance.
More information: <https://docs.mongodb.com/database-tools/mongodump/>.

- Create a dump of all databases (this will place the files inside a directory called "dump"):

`mongodump`

- Specify an output location for the dump:

`mongodump --out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Create a dump of a given database:

`mongodump --db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>

- Create a dump of a given collection within a given database:

`mongodump --collection `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">collection_name</span>` --db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>

- Connect to a given host running on a given port, and create a dump:

`mongodump --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Create a dump of a given database with a given username; user will be prompted for password:

`mongodump --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database</span>` --password`

- Create a dump from a specific instance; host, user, password and database will be defined in the connection string:

`mongodump --uri `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">connection_string</span>
