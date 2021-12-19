---
layout: page
title: common/mongo (English)
description: "MongoDB interactive shell client."
content_hash: 6b32b433167f36ffd365c47c46866fac0af34660
related_topics:
  - title: français version
    url: /fr/common/mongo.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/mongo.html
    icon: bi bi-globe
---
# mongo

MongoDB interactive shell client.
More information: <https://docs.mongodb.com/manual/reference/program/mongo>.

- Connect to a database:

`mongo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database</span>

- Connect to a database running on a given host on a given port:

`mongo --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database</span>

- Connect to a database with a given username; user will be prompted for password:

`mongo --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database</span>` --password`

- Evaluate a JavaScript expression on the database:

`mongo --eval '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">JSON.stringify(db.foo.findOne())</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database</span>
