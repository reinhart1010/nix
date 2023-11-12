---
layout: page
title: common/redis-cli (English)
description: "Opens a connection to a Redis server."
content_hash: d9851d847fbae8dd133a8fc294879f180d30a9d5
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# redis-cli

Opens a connection to a Redis server.
More information: <https://redis.io/topics/rediscli>.

- Connect to the local server:

`redis-cli`

- Connect to a remote server on the default port (6379):

`redis-cli -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Connect to a remote server specifying a port number:

`redis-cli -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Connect to a remote server specifying a URI:

`redis-cli -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uri</span>

- Specify a password:

`redis-cli -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Execute Redis command:

`redis-cli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">redis_command</span>

- Connect to the local cluster:

`redis-cli -c`
