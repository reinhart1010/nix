---
layout: page
title: common/mongosh (English)
description: "A new shell for MongoDB, replacement for `mongo`."
content_hash: 8398a47394b359a266ceeb45eaf470d332439f9b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# mongosh

A new shell for MongoDB, replacement for `mongo`.
Note: all connection options can be replaced with one string: `mongodb://user@host:port/db_name?authSource=authdb_name`.
More information: <https://www.mongodb.com/docs/mongodb-shell>.

- Connect to a local database on the default port (`mongodb://localhost:27017`):

`mongosh`

- Connect to a database:

`mongosh --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">db_name</span>

- Authenticate using the specified username on the specified database (you will be prompted for a password):

`mongosh --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --authenticationDatabase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">authdb_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">db_name</span>

- Evaluate a JavaScript expression on a database:

`mongosh --eval '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">JSON.stringify(db.foo.findOne())</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">db_name</span>
