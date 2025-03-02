---
layout: page
title: common/redis-benchmark (English)
description: "Benchmark a Redis server."
content_hash: 330b1e3187cad939148a04dedb4870c19ccb379b
last_modified_at: 2024-10-11
tldri18n_status: 2
---
# redis-benchmark

Benchmark a Redis server.
More information: <https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/benchmarks/>.

- Run full benchmark:

`redis-benchmark`

- Run benchmark on a specific Redis server:

`redis-benchmark -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Run a subset of tests with default 100000 requests:

`redis-benchmark -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">set,lpush</span>` -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100000</span>

- Run with a specific script:

`redis-benchmark -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100000</span>` script load "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">redis.call('set', 'foo', 'bar')</span>`"`

- Run benchmark by using 100000 [r]andom keys:

`redis-benchmark -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">set</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100000</span>

- Run benchmark by using a [P]ipelining of 16 commands:

`redis-benchmark -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1000000</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">set,get</span>` -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16</span>

- Run benchmark [q]uietly and only show query per seconds result:

`redis-benchmark -q`
