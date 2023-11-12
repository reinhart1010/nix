---
layout: page
title: common/redis-server (English)
description: "Persistent key-value database."
content_hash: 14000b90bee34eb3b252b9631223178d0f386169
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# redis-server

Persistent key-value database.
More information: <https://redis.io>.

- Start Redis server, using the default port (6379), and write logs to `stdout`:

`redis-server`

- Start Redis server, using the default port, as a background process:

`redis-server --daemonize yes`

- Start Redis server, using the specified port, as a background process:

`redis-server --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` --daemonize yes`

- Start Redis server with a custom configuration file:

`redis-server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/redis.conf</span>

- Start Redis server with verbose logging:

`redis-server --loglevel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">warning|notice|verbose|debug</span>
