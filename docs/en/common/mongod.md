---
layout: page
title: common/mongod (English)
description: "The MongoDB database server."
content_hash: 4f147c71076dbc1a9d3e4f400ee7fe027af662da
last_modified_at: 2023-11-12
related_topics:
  - title: Indonesia version
    url: /id/common/mongod.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/mongod.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mongod

The MongoDB database server.
More information: <https://docs.mongodb.com/manual/reference/program/mongod>.

- Specify the storage directory (default: `/data/db` on Linux and MacOS, `C:\data\db` on Windows):

`mongod --dbpath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Specify a config file:

`mongod --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Specify the port to listen on (default: 27017):

`mongod --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Specify the database profiling level. 0 is off, 1 is only slow operations, 2 is all (default: 0):

`mongod --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|1|2</span>
