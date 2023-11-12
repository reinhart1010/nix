---
layout: page
title: common/mongorestore (English)
description: "Utility to import a collection or database from a binary dump into a MongoDB instance."
content_hash: 3ca4c8b9ce669b3d0835a2e97250b44cd8b2f606
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# mongorestore

Utility to import a collection or database from a binary dump into a MongoDB instance.
More information: <https://docs.mongodb.com/database-tools/mongorestore/>.

- Import a BSON data dump from a directory to a MongoDB database:

`mongorestore --db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Import a BSON data dump from a directory to a given database in a MongoDB server host, running at a given port, with user authentication (user will be prompted for password):

`mongorestore --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_host:port</span>` --db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>` --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --password`

- Import a collection from a BSON file to a MongoDB database:

`mongorestore --db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Import a collection from a BSON file to a given database in a MongoDB server host, running at a given port, with user authentication (user will be prompted for password):

`mongorestore --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_host:port</span>` --db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>` --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` --password`
