---
layout: page
title: common/pgbench (English)
description: "Run a benchmark test on PostgreSQL."
content_hash: dca7c2ac421b0f1037b52cc96049f017d0d2d108
---
# pgbench

Run a benchmark test on PostgreSQL.
More information: <https://www.postgresql.org/docs/10/pgbench.html>.

- Initialize a database with a scale factor of 50 times the default size:

`pgbench --initialize --scale=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>

- Benchmark a database with 10 clients, 2 worker threads, and 10,000 transactions per client:

`pgbench --client=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --jobs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` --transactions=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>
