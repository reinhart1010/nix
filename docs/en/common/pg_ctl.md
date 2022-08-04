---
layout: page
title: common/pg_ctl (English)
description: "Utility for controlling a PostgreSQL server and database cluster."
content_hash: 60dbf27c29ffde71fe21220078e0d2c3ce41c0fb
---
# pg_ctl

Utility for controlling a PostgreSQL server and database cluster.
More information: <https://www.postgresql.org/docs/current/app-pg-ctl.html>.

- Initialize a new PostgreSQL database cluster:

`pg_ctl -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data_directory</span>` init`

- Start a PostgreSQL server:

`pg_ctl -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data_directory</span>` start`

- Stop a PostgreSQL server:

`pg_ctl -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data_directory</span>` stop`

- Restart a PostgreSQL server:

`pg_ctl -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data_directory</span>` restart`

- Reload the PostgreSQL server configuration:

`pg_ctl -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data_directory</span>` reload`
