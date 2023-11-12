---
layout: page
title: common/mongo (English)
description: "The legacy MongoDB shell. See `mongosh` for the new shell."
content_hash: 4df61d4e0f31ebfc73b563f489aa0d5d89a69217
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/common/mongo.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/mongo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mongo

The legacy MongoDB shell. See `mongosh` for the new shell.
Note: all connection options can be replaced with one string: `mongodb://user@host:port/db_name?authSource=authdb_name`.
More information: <https://docs.mongodb.com/manual/reference/program/mongo>.

- Connect to a local database on the default port (`mongodb://localhost:27017`):

`mongo`

- Connect to a database:

`mongo --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">db_name</span>

- Authenticate using the specified username on the specified database (you will be prompted for a password):

`mongo --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --authenticationDatabase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">authdb_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">db_name</span>

- Evaluate a JavaScript expression on a database:

`mongo --eval '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">JSON.stringify(db.foo.findOne())</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">db_name</span>
