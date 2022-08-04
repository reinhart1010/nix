---
layout: page
title: common/mongod (English)
description: "The MongoDB database server."
content_hash: 22fda6cdb2850ec6fcd4a3b7128b22d62b358a7b
related_topics:
  - title: Indonesia version
    url: /id/common/mongod.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/mongod.html
    icon: bi bi-globe
---
# mongod

The MongoDB database server.
More information: <https://docs.mongodb.com/manual/reference/program/mongod>.

- Specify a config file:

`mongod --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Specify the port to listen on:

`mongod --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Specify database profiling level. 0 is off, 1 is only slow operations, 2 is all:

`mongod --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|1|2</span>
