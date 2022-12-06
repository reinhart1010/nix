---
layout: page
title: common/mongod (English)
description: "The MongoDB database server."
content_hash: 0da38bc1fd57922d6ff3bbda0025461cffcfdd2a
last_modified_at: 2022-12-06
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

`mongod --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Specify the port to listen on:

`mongod --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Specify database profiling level. 0 is off, 1 is only slow operations, 2 is all:

`mongod --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|1|2</span>
